#!/usr/bin/env python3
"""Generate animated SVG assets for the GitHub profile README."""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONT = "Inter, Arial, Helvetica, sans-serif"
MONO = "JetBrains Mono, SFMono-Regular, Consolas, Liberation Mono, monospace"


def write_svg(name: str, content: str) -> None:
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / name).write_text(content.strip() + "\n", encoding="utf-8")


def text_lines(lines: list[str], x: int, y: int, size: int, color: str, gap: int = 24) -> str:
    spans = []
    for index, line in enumerate(lines):
        dy = 0 if index == 0 else gap
        spans.append(
            f'<tspan x="{x}" dy="{dy}">{escape(line)}</tspan>'
        )
    return (
        f'<text x="{x}" y="{y}" fill="{color}" font-family="{MONO}" '
        f'font-size="{size}" font-weight="700">' + "".join(spans) + "</text>"
    )


def hero() -> str:
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="330" viewBox="0 0 1200 330" role="img" aria-labelledby="title desc">
  <title id="title">Piyush Pathak profile header</title>
  <desc id="desc">Animated brutalist header for a security research GitHub profile.</desc>
  <defs>
    <filter id="shadow" x="-8%" y="-8%" width="116%" height="116%">
      <feDropShadow dx="10" dy="10" stdDeviation="0" flood-color="#facc15"/>
    </filter>
    <linearGradient id="scan" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#67e8f9" stop-opacity="0"/>
      <stop offset="50%" stop-color="#67e8f9" stop-opacity=".9"/>
      <stop offset="100%" stop-color="#67e8f9" stop-opacity="0"/>
    </linearGradient>
    <style>
      @keyframes slide {{ 0% {{ transform: translateX(-260px); }} 100% {{ transform: translateX(1260px); }} }}
      @keyframes blink {{ 0%, 48% {{ opacity: 1; }} 49%, 100% {{ opacity: .18; }} }}
      @keyframes pulse {{ 0%, 100% {{ opacity: .38; }} 50% {{ opacity: 1; }} }}
      .scan {{ animation: slide 3.2s linear infinite; }}
      .blink {{ animation: blink 1s step-end infinite; }}
      .pulse {{ animation: pulse 2s ease-in-out infinite; }}
    </style>
  </defs>
  <rect width="1200" height="330" fill="#050505"/>
  <path d="M0 44H1200M0 286H1200M74 0V330M1128 0V330" stroke="#242424" stroke-width="2"/>
  <rect x="70" y="48" width="1058" height="236" fill="#0a0a0a" stroke="#f8fafc" stroke-width="4" filter="url(#shadow)"/>
  <rect class="scan" x="70" y="48" width="170" height="236" fill="url(#scan)" opacity=".35"/>
  <text x="104" y="104" fill="#facc15" font-family="{MONO}" font-size="18" font-weight="800">SECURITY_RESEARCH_PROFILE</text>
  <text x="104" y="176" fill="#f8fafc" font-family="{FONT}" font-size="58" font-weight="900" letter-spacing="0">PIYUSH PATHAK</text>
  <text x="106" y="224" fill="#67e8f9" font-family="{MONO}" font-size="24" font-weight="800">ANDROID REVERSE ENGINEERING / MALWARE RESEARCH / FULL STACK</text>
  <rect x="1004" y="86" width="72" height="72" fill="#facc15"/>
  <rect class="pulse" x="1018" y="100" width="44" height="44" fill="#050505"/>
  <text class="blink" x="106" y="260" fill="#facc15" font-family="{MONO}" font-size="19" font-weight="800">root@piyush:~$ ./read_systems --verify</text>
</svg>
"""


def section(title: str, index: str, accent: str) -> str:
    safe_title = escape(title.upper())
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="88" viewBox="0 0 1200 88" role="img" aria-label="{safe_title}">
  <style>
    @keyframes dash {{ to {{ stroke-dashoffset: -220; }} }}
    .rail {{ animation: dash 4s linear infinite; }}
  </style>
  <rect width="1200" height="88" fill="#050505"/>
  <rect x="16" y="14" width="1168" height="60" fill="#0a0a0a" stroke="#f8fafc" stroke-width="3"/>
  <rect x="16" y="14" width="94" height="60" fill="{accent}"/>
  <text x="46" y="54" fill="#050505" font-family="{MONO}" font-size="26" font-weight="900">{index}</text>
  <text x="136" y="54" fill="#f8fafc" font-family="{FONT}" font-size="30" font-weight="900" letter-spacing="0">{safe_title}</text>
  <line class="rail" x1="760" y1="44" x2="1162" y2="44" stroke="{accent}" stroke-width="4" stroke-dasharray="28 18"/>
</svg>
"""


def terminal() -> str:
    lines = [
        "status      building reversing labs + security tooling",
        "research    android internals / malware behavior / binary analysis",
        "method      instrument runtime -> inspect memory -> verify output",
        "workflow    linux-first / terminal-heavy / automation-driven",
    ]
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="210" viewBox="0 0 1200 210" role="img" aria-labelledby="title desc">
  <title id="title">Animated terminal field notes</title>
  <desc id="desc">Terminal-style profile notes with blinking cursor and scanning line.</desc>
  <style>
    @keyframes cursor {{ 0%, 48% {{ opacity: 1; }} 49%, 100% {{ opacity: 0; }} }}
    @keyframes glow {{ 0%, 100% {{ opacity: .18; }} 50% {{ opacity: .7; }} }}
    .cursor {{ animation: cursor 1s step-end infinite; }}
    .glow {{ animation: glow 2.4s ease-in-out infinite; }}
  </style>
  <rect width="1200" height="210" fill="#050505"/>
  <rect x="22" y="20" width="1156" height="170" fill="#0a0a0a" stroke="#facc15" stroke-width="3"/>
  <rect x="22" y="20" width="1156" height="34" fill="#facc15"/>
  <circle cx="50" cy="37" r="6" fill="#050505"/>
  <circle cx="74" cy="37" r="6" fill="#050505"/>
  <circle cx="98" cy="37" r="6" fill="#050505"/>
  <text x="128" y="43" fill="#050505" font-family="{MONO}" font-size="15" font-weight="900">field-notes.sh</text>
  <rect class="glow" x="24" y="86" width="1152" height="18" fill="#67e8f9"/>
  {text_lines(lines, 54, 84, 19, "#f8fafc", 28)}
  <rect class="cursor" x="636" y="151" width="12" height="24" fill="#facc15"/>
</svg>
"""


def signal() -> str:
    rows = [
        ("REVERSE ENGINEERING", 86, "#facc15"),
        ("PYTHON AUTOMATION", 74, "#67e8f9"),
        ("FULL STACK", 61, "#f8fafc"),
        ("CTF PRACTICE", 52, "#facc15"),
        ("SYSTEMS RESEARCH", 46, "#67e8f9"),
    ]
    bars = []
    for i, (label, value, color) in enumerate(rows):
        y = 42 + i * 40
        bars.append(f'<text x="44" y="{y + 8}" fill="#f8fafc" font-family="{MONO}" font-size="18" font-weight="800">{label}</text>')
        bars.append(f'<rect x="342" y="{y - 10}" width="760" height="20" fill="#171717" stroke="#3f3f46" stroke-width="2"/>')
        bars.append(f'<rect x="342" y="{y - 10}" width="0" height="20" fill="{color}"><animate attributeName="width" from="0" to="{int(760 * value / 100)}" dur="1.4s" begin="{i * .18}s" fill="freeze"/></rect>')
        bars.append(f'<text x="1120" y="{y + 8}" fill="{color}" font-family="{MONO}" font-size="18" font-weight="900">{value}%</text>')
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="255" viewBox="0 0 1200 255" role="img" aria-labelledby="title desc">
  <title id="title">Current signal bars</title>
  <desc id="desc">Animated skill focus bars for the profile README.</desc>
  <rect width="1200" height="255" fill="#050505"/>
  <rect x="20" y="18" width="1160" height="218" fill="#0a0a0a" stroke="#f8fafc" stroke-width="3"/>
  {"".join(bars)}
</svg>
"""


def footer() -> str:
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="92" viewBox="0 0 1200 92" role="img" aria-label="Profile automation footer">
  <style>
    @keyframes move {{ from {{ transform: translateX(-180px); }} to {{ transform: translateX(1200px); }} }}
    .block {{ animation: move 4s linear infinite; }}
  </style>
  <rect width="1200" height="92" fill="#050505"/>
  <rect x="20" y="18" width="1160" height="56" fill="#facc15"/>
  <rect class="block" x="20" y="18" width="160" height="56" fill="#67e8f9" opacity=".75"/>
  <text x="48" y="54" fill="#050505" font-family="{MONO}" font-size="19" font-weight="900">CI GENERATED PROFILE ASSETS / AUTO REFRESH ENABLED</text>
</svg>
"""


def main() -> int:
    write_svg("hero.svg", hero())
    write_svg("section-about.svg", section("Identity", "01", "#facc15"))
    write_svg("section-stack.svg", section("Stack", "02", "#67e8f9"))
    write_svg("section-ops.svg", section("Operating Areas", "03", "#facc15"))
    write_svg("section-stats.svg", section("Github Telemetry", "04", "#67e8f9"))
    write_svg("section-map.svg", section("Contribution Map", "05", "#facc15"))
    write_svg("section-signal.svg", section("Current Signal", "06", "#67e8f9"))
    write_svg("terminal.svg", terminal())
    write_svg("signal.svg", signal())
    write_svg("footer.svg", footer())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
