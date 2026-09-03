import json
from pathlib import Path
from urllib.parse import urljoin

from markdownify import markdownify
from pelican import signals


class ApiGenerator:
    def __init__(self, context, settings, path, theme, output_path, *args, **kwargs):
        self.context = context
        self.output_path = Path(output_path)
        self.site_url = settings.get("SITEURL", "")

    def generate_output(self, writer):
        payload = {
            "version": "1",
            "contact": {
                "email": "me@duarteocarmo.com",
                "bookingUrl": "https://cal.com/duarteocarmo/meeting?duration=30",
                "consultingUrl": f"{self.site_url}/consulting",
            },
            "posts": [
                self._serialize_content(item=article)
                for article in self.context["articles"]
                if str(article.category) != "photos"
            ],
            "pages": [self._serialize_page(item=page) for page in self.context["pages"]],
        }
        output_path = self.output_path / "api" / "data" / "content.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[api] Wrote {output_path}")

    def _serialize_content(self, *, item) -> dict:
        description = getattr(item, "description", None) or getattr(item, "summary", "")
        serialized = {
            "title": str(item.title),
            "description": markdownify(str(description)).strip().replace("\n", " "),
            "url": urljoin(f"{self.site_url}/", item.url),
            "slug": str(item.slug),
        }
        if hasattr(item, "date"):
            serialized["published"] = item.date.isoformat()
        if hasattr(item, "modified"):
            serialized["updated"] = item.modified.isoformat()
        if hasattr(item, "category"):
            serialized["category"] = str(item.category)
        return serialized

    def _serialize_page(self, *, item) -> dict:
        serialized = self._serialize_content(item=item)
        content = markdownify(str(item.content)).strip()
        serialized["markdown"] = f"# {item.title}\n\n{content}"
        return serialized


def get_generators(_):
    return ApiGenerator


def register():
    signals.get_generators.connect(get_generators)
