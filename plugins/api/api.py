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
        self.site_name = settings.get("SITENAME", "")
        self.site_description = settings.get("SITE_DESCRIPTION", "")

    def generate_output(self, writer):
        payload = {
            "version": "1",
            "profile": {
                "name": self.site_name,
                "description": self.site_description,
                "url": self.site_url,
                "email": "me@duarteocarmo.com",
                "location": "Copenhagen, Denmark",
                "specialties": ["machine learning", "data", "software"],
            },
            "posts": [
                self._serialize_content(item=article)
                for article in self.context["articles"]
                if str(article.category) != "photos"
            ],
            "pages": [self._serialize_content(item=page) for page in self.context["pages"]],
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
        if hasattr(item, "tags"):
            serialized["tags"] = [str(tag) for tag in item.tags]
        return serialized


def get_generators(_):
    return ApiGenerator


def register():
    signals.get_generators.connect(get_generators)
