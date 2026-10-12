# Market research: Ed Briggs Heating & A/C (Fuquay-Varina, NC)

Prepared 11 Oct 2026. Lead from Job finder; approved by Davis directly.

## 1. Lead check: what is happening to edbriggshvac.com

| Question | Evidence | Finding |
|---|---|---|
| Is it Indonesian? | Rendered as US desktop (Chrome, en-US), US iPhone (WebKit) and Googlebot: all three get the same page, title "Beranda \| Ed Briggs Heating & A/C Inc – Layanan Pemanas & AC di Garner, Carolina Utara", Indonesian body. Plain curl with the three user agents: same 107,946 bytes | True, for everyone. No cloaking seen |
| Is it a hacked WordPress? | No. It is not WordPress. The page is a Duda (cdn-website.com) layout, the old Ed Briggs site's own content machine translated, served through Cloudflare | Not a WP hack |
| What is it then? | hreflang en/id/x-default point to https://vac-158.edbriggshvac.com/, which serves an Indonesian lottery/gambling landing page ("TOGEL158", "PORTAL LOGIN", "DAFTAR DISINI") linking to langsung.site and pdmajugroup.online | Domain now used for a gambling site |
| When did it change? | Wayback: real English Ed Briggs site on 5 Jul 2024. Nov 2025 to Feb 2026 the domain shows a GoDaddy parking lander (/lander, img1.wsimg.com/parking-lander). RDAP: registered 10 Jul 2012, expires 10 Jul 2027, last changed 22 Aug 2026, nameservers Cloudflare | Site went dark by late 2025, parked, then re-pointed in Aug 2026 |
| Whose is it now? | Registrant is private. The parked period then new nameservers and a gambling subdomain fit a lapsed domain picked up by a third party, but we can't see the registrant | Very likely no longer controlled by Ed Briggs. Not proven |
| Google results | site:edbriggshvac.com returns nothing in our search tool. Google listing still points to the domain | Listing link goes to the Indonesian copy |
| Rating | 4.8 / 24 on Google, verified via Exa place data. Newest review 1 star, Feb 2024 | Verified |
| SOS, owner, MDN | See FACTS_LOG.md: SOS unconfirmed, no obituary found, no MDN conflict | |

**Verdict: survives, stronger than claimed.** Visitors who click the Website link on Google get an Indonesian copy of the old site from a domain that also hosts a gambling page.

## 2. Top HVAC sites (ranked)
Lighthouse 12 mobile, one run each, 11 Oct 2026.

| Rank | Site | Why | Perf | A11y | BP | SEO | LCP | Weight |
|---|---|---|---|---|---|---|---|---|
| 1 | onehourheatandair.com (national) | Phone and "Schedule" in header, symptom led service menu, guarantee band | 33 | 81 | 75 | 77 | 11.7 s | 2.0 MB |
| 2 | servicechampions.net (regional) | Heating vs cooling split, financing and membership, heavy review proof | 28 | 92 | 68 | 100 | 26.0 s | 6.6 MB |
| 3 | stephensonheatingandair.com (Triangle) | Local family story, service area list, call button everywhere | 57 | 87 | 96 | 77 | 11.4 s | 2.8 MB |
| 4 | thermodirectinc.com (Triangle) | Service agreement pitch, oil and gas heat, emergency line | 32 | 84 | 75 | 100 | 5.4 s | 30.7 MB |
| ref | edbriggshvac.com (current Indonesian copy) | | 51 | 64 | 93 | 92 | 8.6 s | 0.9 MB |
| n/a | aire-serv.com | Blocked headless Chrome (interstitial); not scored | | | | | | |

## 3. Patterns used
- Heating vs cooling split up front (Service Champions): the dual hero.
- Phone in header plus sticky phone bar (all).
- Owner and history as trust (Stephenson): since 1960, J. Edward Briggs.
- Specialty and service agreements (Thermo Direct): oil furnace and boiler card, maintenance row.
- Not copied: financing, memberships, guarantees, 24/7 promises beyond what the old site said.
