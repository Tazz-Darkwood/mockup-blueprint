---
name: Sales (a purpose guide)
summary: Stack on top of the general style guide when the site exists to sell products. Says what a shop must show and where, which parts carry the look and which stay conventional. The specifics belong to each site's own guide.
kind: purpose
detect: []
checked: 2026-10-03
source: a study of seven shops and two bodies of usability research, listed at the end
---

# Sales

A purpose guide. It is stacked on `style-guide.md` (the general guide) when a site's job is to sell things, usually alongside a feel guide such as `style-feel-artistic.md`. It gives way to the site's own guide wherever that is more specific. The general guide's accessibility minimums still hold.

Like the feel guides, this one does not describe a look. Seven shops selling natural body care were studied, from a soap maker with almost no text on the page to a high-street chain, and they look very different. What they share is **what a shopper is shown at each step, and how conventional the buying steps are**. Even the most artistic of them switch to a plain, familiar layout the moment the shopper is deciding to buy.

## When sales and a feel guide are both stacked

**Sales reaches only as far as the buying steps**: what a product tile must show, how the product page is arranged, the basket and the checkout. On those, convention beats expression. Everything else on the site, the top of the home page, the sections between, the story, the footer, the pictures, the typeface, the colour and the voice, belongs to the feel guide. If the brief says otherwise for a particular site, the brief wins.

This was learned the hard way. On the first Greenfire Herbs mockup, "quiet and conventional" was applied to the whole site and the result was judged "too clean and cold, more like a professional site" for one person making soap at home. The buying steps were right; the reach was wrong.

## The detail map for a shop

Levels are the three from the general guide: signature, styled, quiet.

| Part of the site | Level | What it must contain | Seen on |
|---|---|---|---|
| Top of the home page | Signature | The product itself, photographed in a scene, with a short line of text and one "shop" button | 7 of 7 (button on 6) |
| Product tile | Styled, and identical for every product | A picture on a plain, consistent background; the name; the price | 6 of 7; price on the tile on 5 |
| First row under the top | Styled | Actual products or categories, reachable in one click | 6 of 7 |
| Navigation | Quiet and conventional | Product categories, search, and the basket at the top right | 7 of 7 |
| Product page | Quiet and conventional | Two columns: pictures on one side; name, price, options, quantity and one add button on the other | 5 of 5 |
| Facts a shopper checks | Quiet, but present and near the add button | Ingredients, delivery, returns | Delivery 5 of 5, ingredients 4 of 5 |
| Reviews | Quiet | A rating near the name | 3 of 5 |
| Announcement strip | Quiet | One line above the header, usually the free-delivery threshold | 5 of 7 |
| Basket and checkout | Quiet and conventional | Not studied; from the research below | |

## Use it properly

1. In the brief, say what is sold, to whom, and how they pay.
2. List the real products first, with names and prices, before any layout. A shop mockup without products is a brochure.
3. Design one product tile and one product page. Everything else follows from those two.
4. Before showing the mockup, walk the buying path as a stranger: from the first screen to a product, to the basket, to paying. Count the clicks and note every point where a fact was missing.

## Notes

### The first screen shows the product and one way in
- Status: draft
- Source: study, 7 of 7 opened on a photograph with the products in it; 6 of 7 put a short line and a single shop button over it; 6 of 7 followed it immediately with a row of products or categories.
- Rule: a visitor can tell what is sold without scrolling, and can reach a product in one click. The top is a picture of the goods, not an abstract mood.

### Every product tile shows a picture, the name and the price
- Status: draft
- Source: study, 6 of 7 used the same plain background for every product picture; 5 of 7 showed the price on the tile. Nielsen Norman Group lists a descriptive name, a recognisable image and the price as the essentials.
- Rule: tiles are identical in layout and each carries those three things. A shopper compares tiles; anything that differs between them should be the product, not the design.

### The product page is conventional
- Status: draft
- Source: study, 5 of 5, including the most artistic shops. Pictures on one side; on the other the name, price, options, quantity and one wide add button, in that order. The add button was visible without scrolling on 4 of 5.
- Rule: do not reinvent this page. Two columns, the add button in the first screen, one add button. The site's character shows in the photographs, the type and the colour, not in the arrangement.

### Conventional is about where things are, not how polished they look
- Status: draft
- Source: the owner's critique of the first Greenfire Herbs mockup, 2026-10-03, and the second version that followed
- Rule: on the buying steps the arrangement stays familiar and every fact stays easy to read: picture, name, price, one add button, costs stated. Within that, the surface can carry the site's character. On Greenfire the price sits on a hand-written tag and the picture is taped to a card, and the product page is still the standard two columns.
- Why: shoppers rely on finding things in the usual place. They do not rely on everything being plain.

### Say what it costs, all of it, before the basket
- Status: draft
- Source: Nielsen Norman Group ("price, including any additional product-specific charges"; show delivery costs on the product page, not hidden until checkout; hidden costs found at checkout damage trust). Study: all 5 product pages mentioned delivery.
- Rule: the product page states the price and what delivery costs or when it is free. Nothing is added later that was not announced here.

### Adding to the basket is confirmed, clearly
- Status: draft
- Source: Nielsen Norman Group ("inadequate feedback caused many problems. Some users thought they had added items when they had not"; use a confirmation or a conspicuous persistent notice).
- Rule: after pressing add, the shopper sees what was added and the basket's new count. The basket is always one click away, top right.

### The facts a shopper checks sit next to the add button
- Status: draft
- Source: study, 4 of 5 product pages listed ingredients, 5 of 5 delivery; three used collapsible sections under the add button (details, how to use, ingredients). Nielsen Norman Group: "be complete, but not wordy or fluffy"; insufficient information makes shoppers abandon.
- Rule: for each product, write the facts someone needs before buying (for soap: ingredients, size or weight, scent, who it suits) in plain sentences, and put them under the add button. No marketing filler.

### Options and availability are explicit
- Status: draft
- Source: Nielsen Norman Group (clear options and a way to select them; "communicate product availability"; the same information for every variation).
- Rule: sizes, scents and quantities are visible choices, not hidden in a menu, and something out of stock or made to order says so before the shopper commits.

### The pictures do the selling, so they must be real
- Status: draft
- Source: Baymard Institute's homepage benchmark (sites with "good design and inspiring photography" drew positive remarks; stock or "bland and boring cut out imagery" underperformed; 19% of sites lacked bespoke imagery). Nielsen Norman Group: one view is rarely enough.
- Rule: a shop needs its own photographs, several per product. In a mockup, draw or stand in for them and write in the blueprint exactly which photographs the real site needs. They block the launch.

### No pop-up on arrival, and no rotating banner at the top
- Status: draft
- Source: Baymard Institute (59% of sites had overly aggressive promotions, with newsletter pop-ups singled out; 75% of sites using carousels implemented them badly, and static sections often do better). Study: two of the seven covered the page with a newsletter pop-up within seconds.
- Rule: nothing covers the page uninvited. The top is one still image. A newsletter sign-up lives in the page, usually near the foot.

### Show the range, not one product
- Status: draft
- Source: Baymard Institute (shoppers misjudged what a site sold when the home page showed too little; feature a broad range with thumbnails or links).
- Rule: the home page shows enough different products or categories for a visitor to grasp the whole range.

### Reviews are never invented
- Status: draft
- Source: Nielsen Norman Group (reviews are valuable and shoppers look for the negative ones); the rule against invented ones is judgement.
- Rule: a mockup may show where reviews go, clearly marked as samples. The blueprint says they must be real, and what happens when there are none yet.

### Do not copy the small print
- Status: draft
- Source: study. Body text was 14px or smaller on 5 of 7, and 11px on one.
- Rule: shops routinely set text below the general guide's minimum. The minimum holds.

## Not covered yet

- The basket and checkout pages were not studied.
- Phone layouts were not studied.
- All seven shops sell similar goods. Shops selling one large item, services, or digital goods may differ.

## How these notes get approved

A note here is approved when it has held on two different shops built with this guide and the skill's owner has agreed with the result on both.

## Sources

Studied on 2026-10-03 by opening each site in a browser at 1440 pixels wide: Binu Binu (binu-binu.com), Meow Meow Tweet (meowmeowtweet.com), Fat and the Moon (fatandthemoon.com), Flamingo Estate (flamingoestate.com), Herbivore (herbivorebotanicals.com), Lush (lush.com), Aesop (aesop.com). Product pages were seen for five of them. An eighth site redirected elsewhere and was dropped. These were chosen as known, well-regarded shops in the same trade, not from an award list.

Research read the same day: Nielsen Norman Group, "UX guidelines for ecommerce product pages"; Baymard Institute, homepage and category benchmark (figures from its 2020 benchmark of 60 sites). A third Baymard article, on product pages, could not be read.

## Questions it raises

- How do people pay: on the site, or by arrangement afterwards?
- What does delivery cost, and where is it offered?
- What can be returned?
- Who takes the product photographs, and when?
- Are there real reviews to show?
