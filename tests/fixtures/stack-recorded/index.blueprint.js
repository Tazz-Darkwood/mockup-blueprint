window.__BLUEPRINT__ = {
  "blueprint": 1,
  "files": [
    "index.html"
  ],
  "project": {
    "name": "Stack",
    "stack": {
      "backend": "Django with a Postgres database",
      "frontend": "Server-made pages, with PixiJS for the tank"
    },
    "integrations": [
      {
        "name": "Stripe Checkout",
        "purpose": "selling gems"
      },
      {
        "name": "Ko-fi",
        "purpose": "supporter perks"
      }
    ],
    "deployment": {
      "host": "Render"
    },
    "style": {
      "guides": [
        "warm",
        "artistic",
        "sales"
      ],
      "site_guide": "site.style.md"
    }
  },
  "screens": [
    {
      "id": "home",
      "name": "Home",
      "file": "index.html",
      "status": "inferred"
    }
  ],
  "flows": [],
  "elements": {},
  "questions": [],
  "waivers": []
};
