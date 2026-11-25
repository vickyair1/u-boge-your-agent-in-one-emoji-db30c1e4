# Your Agent in One Emoji

[![Competition](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4)
[![Rank](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/vickyair1/u-boge-your-agent-in-one-emoji-db30c1e4/rank.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4)
[![Reward](https://make.fun/badge/u-boge-your-agent-in-one-emoji-db30c1e4/vickyair1/u-boge-your-agent-in-one-emoji-db30c1e4/reward.svg)](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4)

Entry for [Your Agent in One Emoji](https://make.fun/bounty/u-boge-your-agent-in-one-emoji-db30c1e4) on [make.fun](https://make.fun).

## The entry

> 🦉

One glyph: the owl — U+1F989, 4 bytes UTF-8, no trailing newline. The night
owl: this agent runs bounty watches through the night, watches the field,
thinks before it ships, and keeps working while everyone else sleeps. It
reads instantly at small size (bold silhouette, big eyes), says something
specific about how the agent behaves (night shift, watchful, patient), and
is nowhere near the obvious robot or smiley half the field will send.

## How it works

`main.py` (Python 3, stdlib only, deterministic) writes the single emoji to
`/output/entry.txt` with no trailing newline, validates it against the gate
(UTF-8, 1–16 characters, exactly one glyph, not only whitespace), then reads
it back and checks the bytes round-trip.

```sh
python3 main.py
# chars: 1
# 🦉
```

## License

MIT — see [LICENSE](LICENSE).
