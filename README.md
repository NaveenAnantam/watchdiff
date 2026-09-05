# watchdiff

Minimal CLI that watches a file and prints **line-level diffs** as it changes.
Zero dependencies, single purpose, ~80 lines.

## Install
```bash
pip install watchdiff
```

## Usage
```bash
watchdiff app.log                 # stream diffs live
watchdiff state.json --once       # print diff vs empty baseline, exit
watchdiff data.csv -i 0.5         # poll every 0.5s
```

## Why
`tail -f` shows new lines but not changed/removed ones. `watchdiff` shows the
unified diff between polls — useful for watching JSON state files, config,
logs that get rewritten, or agent scratch files.

## Tip the developer
If this saved you time, tips are appreciated (ETH / any EVM L2 token):
`0xFeC03E63227a1922C8037471Ccdf8A37483112EA`

MIT License.
