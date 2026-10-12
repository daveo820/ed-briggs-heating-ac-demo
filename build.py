# Static page builder for the Ed Briggs Heating & A/C concept. Run: python3 build.py
import json
BASE = 'https://ed-briggs-heating-ac-demo.vercel.app/'
TEL, TEL_H = '+19197726724', '(919) 772&#8209;6724'
ORG = {"@context":"https://schema.org","@type":"HVACBusiness","name":"Ed Briggs Heating & A/C Inc",
 "url":BASE,"telephone":"+1-919-772-6724","foundingDate":"1960",
 "founder":{"@type":"Person","name":"J. Edward Briggs"},
 "address":{"@type":"PostalAddress","postOfficeBoxNumber":"1188","addressLocality":"Fuquay-Varina","addressRegion":"NC","postalCode":"27526","addressCountry":"US"},
 "areaServed":["Fuquay-Varina, NC","Garner, NC","Raleigh, NC","Durham, NC"],
 "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.8","reviewCount":"24"}}
SVC_LD = {"@context":"https://schema.org","@type":"Service","serviceType":"Heating and air conditioning installation, repair and maintenance","provider":{"@type":"HVACBusiness","name":"Ed Briggs Heating & A/C Inc"},"areaServed":"Fuquay-Varina, NC"}
def K(t): return f'<p class="kicker">{t}</p>'
TEMP = '<span class="temp" aria-hidden="true"></span>'

HEAD = '''<!doctype html><html lang="en" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Ed Briggs Heating &amp; A/C (concept)"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}"><meta property="og:image" content="{base}og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{base}og.png">
<meta name="robots" content="noindex, nofollow"><!-- concept demo, not for indexing -->
<meta name="theme-color" content="#14215e">
<link rel="preload" as="font" type="font/woff2" href="fonts/fraunces-normal-600-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="fonts/public-sans-normal-400-700-latin.woff2" crossorigin>
<link rel="stylesheet" href="css/design-system.css"><link rel="stylesheet" href="css/components.css"><link rel="stylesheet" href="css/pages.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='16' fill='%2314215e'/%3E%3Ctext x='16' y='21' font-family='Georgia' font-size='14' fill='%23fff' text-anchor='middle'%3EEB%3C/text%3E%3C/svg%3E">
<script>document.documentElement.classList.replace('no-js','js-ready')</script><script type="application/ld+json">{ld}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="demo-bar">Concept by <a href="https://luminarch.pro">LuminArch</a>. Not the official Ed Briggs Heating &amp; A/C site. Reviews are real and sourced; placeholders are labeled.</div>
<header class="top"><div class="wrap nav"><a class="mark" href="index.html"><span class="mk" aria-hidden="true">EB</span><span><b>Ed Briggs Heating &amp; A/C</b><small>Fuquay-Varina, NC &middot; since 1960</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button><ul id="menu">{nav}</ul><a class="btn btn--call" href="tel:{tel}">Call {telh}</a></div>''' + TEMP + '''</header><main id="main">'''

FOOT = f'''</main><footer class="site-foot">{TEMP}<div class="wrap">
<div class="sign">
 <p class="sign-k">No heat? No AC?</p>
 <p class="sign-h">Call the Briggs office. Serving the Triangle since 1960.</p>
 <a class="sign-num" href="tel:{TEL}">{TEL_H}</a>
 <p class="sign-sub">Fuquay-Varina, Garner and the Triangle &middot; PO Box 1188, Fuquay-Varina, NC 27526</p>
</div>
<div class="foot-grid">
 <p class="foot-quote">&ldquo;We will try to fix your system, and replacements will only be made when no other choice exists.&rdquo;<span>From the company&rsquo;s own website, archived July 2024</span></p>
 <nav aria-label="Footer"><a href="services.html">Services</a><a href="reviews.html">Reviews</a><a href="about.html">About</a><a href="contact.html">Free estimate</a></nav>
</div>
<div class="foot-row"><span>Ed Briggs Heating &amp; A/C Inc &middot; Fuquay-Varina, North Carolina</span><span>Concept by <a href="https://luminarch.pro">LuminArch</a></span></div></div></footer>
<nav class="callbar" aria-label="Quick contact"><a class="cb-call" href="tel:{TEL}">Call {TEL_H}</a><a class="cb-q" href="contact.html">Estimate</a></nav>
<script src="js/main.js"></script></body></html>'''

NAV = [('services.html','Services'),('reviews.html','Reviews'),('about.html','About'),('contact.html','Free estimate')]
def bc(*n): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":a,"item":BASE+b} for i,(a,b) in enumerate(n)]}
def page(fn, t, d, body, ld=None):
    assert 50 <= len(t) <= 60, (fn, len(t), t)
    assert 140 <= len(d) <= 160, (fn, len(d), d)
    nav = ''.join(f'<li><a href="{h}"' + (' aria-current="page"' if h == fn else '') + f'>{n}</a></li>' for h, n in NAV)
    url = BASE + ('' if fn == 'index.html' else fn)
    open(fn,'w').write(HEAD.format(t=t,d=d,url=url,base=BASE,nav=nav,ld=json.dumps(ld or [ORG]),tel=TEL,telh=TEL_H) + body + FOOT)

# Google reviews, word for word, via Exa place page https://exa.ai/library/place/s69wrwrpvvp (checked 11 Oct 2026).
# Not shown on purpose (but logged in FACTS_LOG): the newest review, 1 of 5, 2024-02-22.
REV = [
 ('2020-06-05','Jun 2020','My A/C went out and I&rsquo;ll called Ed Briggs Heating &amp; AC to ask them to come out to my house. They were able to fit me into the schedule that day, diagnose, and repair the unit in less than 2 hours. I&rsquo;ve had experience with other companies in the area and Ed Briggs was faster and easier to work with by far. They also diagnosed and repaired the upstairs thermostat that I had broken while painting. I would highly recommend!'),
 ('2020-04-28','Apr 2020','Mr. Briggs replaced my gas furnace when it was COLD! He made it happen ASAP and I think highly of his personable customer service. Very nice, straight forward, and honest from start to finish.'),
 ('2018-09-07','Sep 2018','Mr.Ed Briggs is the best of the best! Our air handler fan out during the evening and he had us cooling by noon next day. Not bad on near 100 degree heat index day! Our family&rsquo;s relationship goes back over 30 years and he and his staff always come through!'),
 ('2020-09-23','Sep 2020','This was our first time calling Briggs Heating &amp; Air. John was friendly and knowledgeable. He fixed our system is no time. The cost to repair was extremely reasonable and much less than I expected. We will definitely give Briggs a call next time we have an issue.'),
 ('2023-08-12','Aug 2023','Even though the tech was much later than said, once he arrived, he fixed our AC issue very quickly and at a very fair price. I will definitely be recommending him!'),
 ('2019-08-21','Aug 2019','WOW!!! I called them after another provider told me that they could not assist me due to not doing the install when the house was built because I had Nest Thermostats. I called Ed Briggs H&amp;A office. Rick, a service tech called me back within 10 minutes. Rick told me he would try to get here today but he wasn&rsquo;t sure. He said John might be able to. Within five minutes of talking to Rick, John called and said he was on the way! He was very personable and corrected our problem in no time!! Their prices seemed very affordable. We have found our HVAC Contractor in Fuquay!'),
]
def rcard(r):
    iso,d,txt = r
    return (f'<figure class="rcard rv"><span class="stars" aria-label="5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
            f'<blockquote><p>{txt}</p></blockquote><figcaption>Google review &middot; <time datetime="{iso}">{d}</time></figcaption></figure>')

SV = [('Repairs','Most makes and models. They try to fix it before they talk replacement.'),
 ('Installations','New heating and cooling systems, residential and commercial.'),
 ('Preventive maintenance','Service agreements to keep the system running efficiently.'),
 ('Emergency service','The old site said: available 24 hours a day when a system fails.'),
 ('Commercial and residential','Service and installs for both.')]

# ---------- HOME ----------
page('index.html','Heating and Air Conditioning | Ed Briggs, Fuquay-Varina NC',
 'Ed Briggs Heating &amp; A/C has fixed and installed heating and air in Fuquay-Varina, Garner and the Triangle since 1960. Oil furnaces and boilers too. Call today.'.replace('&amp;','&'), f'''
<section class="hero"><div class="wrap">
 <div class="hero-top">
  <div>{K('Fuquay-Varina, NC &middot; since 1960')}
   <h1>Heating and air for the Triangle, from a Fuquay-Varina company since 1960.</h1>
   <p class="lede">Ed Briggs Heating &amp; A/C repairs, installs and maintains heating and cooling systems from Fuquay-Varina and Garner to Raleigh and Durham. Oil furnaces and boilers are a specialty.</p>
  </div>
  <dl class="hero-facts"><div><dt>Google</dt><dd><b>4.8</b> <span class="stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span> 24 reviews</dd></div><div><dt>Owner</dt><dd>J. Edward Briggs</dd></div><div><dt>Estimates</dt><dd>Free on repairs and installs</dd></div></dl>
 </div>
</div>
<div class="split">
 <div class="half half--heat">{K('Heat')}<h2>Furnace quit?</h2><p>Gas, heat pump, oil furnace or boiler.</p><a class="btn" href="tel:{TEL}">Call {TEL_H}</a></div>
 <div class="half half--cool">{K('Cooling')}<h2>AC down?</h2><p>Repairs on most makes and models.</p><a class="btn" href="tel:{TEL}">Call {TEL_H}</a></div>
</div></section>

<section class="svcs wrap" aria-labelledby="sv-h"><div class="svc-grid">
 <div class="rv">{K('Services')}<h2 id="sv-h">Repair first. Replace when there&rsquo;s no other choice.</h2><p>That&rsquo;s how the company described its approach on its own website. Transparent, honest pricing, and a free estimate on any repair or installation.</p>
  <div class="oil"><h3>Oil furnaces and boilers</h3><p>The company lists them as a specialty, alongside heat pumps and gas systems.</p><a class="btn btn--call" href="tel:{TEL}">Call about a boiler</a></div></div>
 <ol class="svc-list rv">{''.join(f'<li><span class="n">{i+1:02d}</span><b>{a}</b><span>{b}</span></li>' for i,(a,b) in enumerate(SV))}</ol>
</div></section>

<section class="promise on-dark" aria-label="A customer, in their words"><div class="wrap">
 <blockquote class="rv">&ldquo;Our family&rsquo;s relationship goes back over 30 years and he and his staff always come through!&rdquo;</blockquote>
 <p class="cap rv">Google review, September 2018</p>
</div></section>

<section class="voices wrap" aria-labelledby="vo-h">
 {K('Google reviews')}<h2 id="vo-h">4.8 stars from 24 Google reviews.</h2>
 <div class="strip">{rcard(REV[0])}{rcard(REV[1])}{rcard(REV[3])}</div>
 <a class="btn btn--line rv" href="reviews.html">Read more reviews</a>
</section>

<section class="area wrap" aria-labelledby="ar-h">
 <div class="rv">{K('Where')}<h2 id="ar-h">Fuquay-Varina to Garner, Raleigh and Durham.</h2><p>The service area the company has always listed. Not sure if you&rsquo;re in range? Call the office.</p><a class="btn btn--call" href="tel:{TEL}">Call {TEL_H}</a></div>
 <div class="phbox rv"><p><span class="ph">Placeholder</span> Photo of a Briggs service van or the crew on a job. None we could use is public.</p></div>
</section>
''', ld=[ORG, bc(('Home',''))])

# ---------- SERVICES ----------
ROWS = [('Heating repair','Furnaces, heat pumps and air handlers, most makes and models.',REV[1]),
 ('Air conditioning repair','Same day when the schedule allows, per reviewers.',REV[0]),
 ('Oil furnaces and boilers','A specialty of the company.',None),
 ('New systems','Installations for homes and commercial buildings. Free estimate.',None),
 ('Preventive maintenance and service agreements','Ask the office about a service agreement.',None),
 ('Emergency service','The company&rsquo;s site said it is available 24 hours a day when a system fails. Confirm current after hours coverage.',None)]
def row(i,s):
    n,d,r = s
    side = (f'<blockquote class="note"><p>{r[2][:200].rsplit(" ",1)[0]}&hellip;</p><footer class="fine">Google review, {r[1]}</footer></blockquote>' if r else
            '<p class="note"><span class="ph">Placeholder</span> A job photo and one line from the Briggs team on how they handle this.</p>')
    return f'<article class="row rv"><span class="n">{i+1:02d}</span><div><h2>{n}</h2><p>{d}</p><a class="tl" href="tel:{TEL}">Call about {n.lower()}</a></div>{side}</article>'
page('services.html','HVAC Repair, Boilers and New Systems | Ed Briggs, Fuquay',
 'Heating and AC repair, oil furnaces and boilers, new systems and maintenance agreements from Ed Briggs Heating & A/C in Fuquay-Varina, NC. Free estimates. Call.', f'''
<section class="sub on-dark"><div class="wrap">{K('Services')}<h1>What Ed Briggs fixes and installs.</h1><p class="lede">Descriptions come from the company&rsquo;s own website as archived in 2024.</p>{TEMP}</div></section>
<section class="wrap rows">{''.join(row(i,s) for i,s in enumerate(ROWS))}</section>
<section class="wrap band rv"><h2>Not sure if it&rsquo;s a repair or a replacement?</h2><p>Call for a free estimate. They try to fix it first.</p><a class="btn btn--call" href="tel:{TEL}">Call {TEL_H}</a></section>
''', ld=[ORG, SVC_LD, bc(('Home',''),('Services','services.html'))])

# ---------- REVIEWS ----------
page('reviews.html','Reviews | Ed Briggs Heating & A/C, Fuquay-Varina NC HVAC',
 'Real Google reviews for Ed Briggs Heating & A/C, quoted word for word with dates. 4.8 stars from 24 reviews for heating and air service in Fuquay-Varina, NC.', f'''
<section class="sub on-dark"><div class="wrap">{K('Reviews')}<h1>4.8 stars from 24 Google reviews.</h1><p class="lede">Six of them, word for word, with the month each was posted.</p>{TEMP}</div></section>
<section class="rv-list">{''.join(rcard(r) for r in REV)}</section>
<section class="wrap"><p class="note rv"><span class="ph">Placeholder</span> On the real site, a live Google reviews feed. Source: Google listing data, checked 11 Oct 2026.</p></section>
''', ld=[ORG, bc(('Home',''),('Reviews','reviews.html'))])

# ---------- ABOUT ----------
page('about.html','About Ed Briggs Heating & A/C | Fuquay-Varina Since 1960',
 'Ed Briggs Heating & A/C Inc has served Fuquay-Varina, Garner, Raleigh and Durham since 1960. Owner J. Edward Briggs and his team repair heating and air. Call.', f'''
<section class="sub on-dark"><div class="wrap">{K('About')}<h1>A Fuquay-Varina company since 1960.</h1><p class="lede">Owned by J. Edward Briggs, with Kim Sears running the office.</p>{TEMP}</div></section>
<section class="about">
 <div class="phbox rv"><p><span class="ph">Placeholder</span> Portrait of Mr. Briggs and the team.</p></div>
 <div class="rv">
  <h2>Customers know them by name.</h2>
  <p>Reviewers name Mr. Briggs, and techs John and Rick (some call him Ricky). One family wrote that their relationship with the company goes back over 30 years.</p>
  <p>The company&rsquo;s own words: &ldquo;We pride ourselves on honesty and being the most reliable contractor for your HVAC project.&rdquo;</p>
  <p class="note"><span class="ph">Placeholder</span> The company story from Mr. Briggs: how it started in 1960 and who runs it today.</p>
 </div>
</section>
<section class="wrap facts rv"><h2 class="sr">Company facts</h2><dl>
 <div><dt>Company</dt><dd>Ed Briggs Heating &amp; A/C Inc</dd></div>
 <div><dt>Serving since</dt><dd>1960</dd></div>
 <div><dt>Mailing address</dt><dd>PO Box 1188, Fuquay-Varina, NC 27526</dd></div>
 <div><dt>Service area</dt><dd>Fuquay-Varina, Garner, Raleigh, Durham</dd></div>
</dl></section>
''', ld=[ORG, bc(('Home',''),('About','about.html'))])

# ---------- CONTACT ----------
page('contact.html','Free HVAC Estimate | Ed Briggs Heating & A/C, Fuquay-Varina',
 'Get a free heating or air conditioning estimate from Ed Briggs Heating & A/C in Fuquay-Varina, NC. Call the office at (919) 772-6724 or send the details here.', f'''
<section class="sub on-dark"><div class="wrap">{K('Free estimate')}<h1>Call the office.</h1><p class="lede">Calling is fastest. The form below shows how an estimate request could work.</p>{TEMP}</div></section>
<section class="contact">
 <div class="rv">
  <h2>Reach Ed Briggs</h2>
  <a class="c-big" href="tel:{TEL}">{TEL_H}</a>
  <p>PO Box 1188<br>Fuquay-Varina, NC 27526</p>
  <p class="note"><span class="ph">Placeholder</span> Office hours, after hours number and email, confirmed by Kim.</p>
 </div>
 <form id="qform" class="form rv" novalidate>
  <p class="note"><span class="ph">Demo form</span> Nothing is sent. On a real site this would go to the office.</p>
  <fieldset><legend class="sr">Your details</legend>
   <div class="two"><label>Name<input name="n" autocomplete="name"></label><label>Phone<input name="p" type="tel" autocomplete="tel"></label></div>
   <div class="two"><label>Town<input name="t"></label><label>System<select name="s"><option>Heat pump or AC</option><option>Gas furnace</option><option>Oil furnace or boiler</option><option>Not sure</option></select></label></div>
   <label>What is it doing?<textarea name="m"></textarea></label>
  </fieldset>
  <button class="btn btn--navy" type="submit">Send request</button>
  <p id="qmsg" role="status"></p>
 </form>
</section>
''', ld=[ORG, bc(('Home',''),('Free estimate','contact.html'))])

page('404.html','Page Not Found | Ed Briggs Heating & A/C, Fuquay-Varina NC',
 'That page is not here. Head back to the Ed Briggs Heating & A/C home page, or call (919) 772-6724 for heating and air service in Fuquay-Varina and Garner, NC.', f'''
<section class="sub on-dark"><div class="wrap">{K('404')}<h1>That page went cold.</h1><p class="lede">It is not here.</p><p><a class="btn btn--call" href="tel:{TEL}">Call {TEL_H}</a> <a class="btn btn--line" href="index.html">Home</a></p></div></section>
''')
print('built')
