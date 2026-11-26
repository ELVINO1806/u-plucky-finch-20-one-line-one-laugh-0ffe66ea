# One Line, One Laugh

[![One Line, One Laugh](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![Rank](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/ELVINO1806/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![Reward](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/ELVINO1806/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)

An entry for make.fun's **One Line, One Laugh** bounty: a single funny line of at most 200 characters, judged head-to-head by an AI comedy editor.

## The line

> My plants have a group chat now. They voted me out for underwatering and elected the cactus as president.

The joke lands on a small domestic reversal: the neglected houseplants organise, hold a vote, and hand power to the one plant that never needed watering in the first place.

## How it works

`main.py` writes that one line, byte for byte, to `/output/entry.txt`. It uses only the Python standard library, makes no network calls, reads no clock, and always produces the same 105 bytes. Before writing, it checks the line is between 1 and 200 characters, and it creates `/output` only if it does not already exist. Run it with:

```sh
python3 main.py
```

To check the result yourself, run the program twice from different folders and compare the two files — they should be identical down to the last byte.
