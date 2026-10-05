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
  "elements": {
    "scene": {
      "name": "The study",
      "does": "The first screen.",
      "status": "inferred",
      "picture": {
        "shows": "A harbour at dusk, lit by one lamp."
      }
    },
    "map": {
      "name": "The map",
      "does": "Shows the valley.",
      "status": "inferred",
      "picture": {
        "shows": "A map.",
        "made": "Drawn in code.",
        "page_relies_on": "nothing"
      }
    }
  },
  "questions": [],
  "waivers": []
};
