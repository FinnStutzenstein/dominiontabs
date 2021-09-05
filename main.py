import domdiv.main

base_args = [
   "--papersize", "A4",
   "--language", "de",
   "--size", "9.5x6.25",
   "--types",
   "--tab-side", "left-alternate",
   "--tabwidth", "4.0",
   "--tab-name-align", "center",
   "--order", "cost",
   "--expansion-dividers",
   "--centre-expansion-dividers",
   "--expansion-reset-tabs",
   "--expansions", "base", "alchemy", "cornucopia", "dark ages", "dominion2ndEdition", "empires", "promo",
   "--no-trash",
   "--group-kingdom",
   "--group-special",
]
opts = domdiv.main.parse_opts(base_args)
opts = domdiv.main.clean_opts(opts)
domdiv.main.generate(opts)
