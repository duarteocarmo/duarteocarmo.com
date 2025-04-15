from datetime import datetime
from pathlib import Path

from markdownify import markdownify as md
from pelican import contents, signals


class LLMSGenerator:
    def __init__(self, context, settings, path, theme, output_path, *args, **kwargs):
        self.context = context
        self.settings = settings
        self.output_path = Path(output_path)
        self.siteurl = settings.get("SITEURL", "")
        self.sitename = settings.get("SITENAME", "My Site")
        self.site_description = settings.get("SITE_DESCRIPTION", "")
        self.now = datetime.now()

    def generate_output(self, writer):
        about_content = self._get_about_summary()
        pages = self.context.get("pages", [])
        articles = self.context.get("articles", [])

        lines = [f"# {self.sitename} - {self.site_description}", ""]
        lines.append(about_content)
        lines.append("")

        if pages:
            lines.append("## Pages")
            for page in pages:
                lines.append(self._format_entry(page))
            lines.append("")

        if articles:
            lines.append("## Posts")
            for article in articles:
                if article.category == "photos":
                    continue
                lines.append(self._format_entry(article))
            lines.append("")

        llms_txt_path = self.output_path / "llms.txt"
        llms_txt_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"[llms_txt] Wrote {llms_txt_path}")

    def _get_about_summary(self) -> str:
        about_page = next(
            (p for p in self.context.get("pages", []) if p.slug == "about"), None
        )
        if not about_page:
            return f"> No description available for {self.sitename}."
        content = md(about_page.content)
        content = content.strip().replace("\n", " ")

        return f"> {content}"

    def _format_entry(self, item: contents.Content) -> str:
        return f"- [{item.title}]({self.siteurl}/{item.url}.md)"


def get_generators(_):
    return LLMSGenerator


def register():
    signals.get_generators.connect(get_generators)
