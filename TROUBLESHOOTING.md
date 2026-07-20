# Troubleshooting

## Skill loads, but action `analyze` fails

Cause: the model generated an unsupported tool/action call. Text-only skills do not have an `analyze` executable.

Mitigations:

- update the skill to version 3;
- remove the old skill and add it again;
- start a new chat;
- enable only one text skill;
- paste text instead of attaching an image;
- use Ask Image separately for OCR.

## Law lookup does not run

Check:

- `russian-law-search` is enabled;
- the device has internet access;
- a valid Tavily API key was entered;
- the model called `run_js`, not `analyze`;
- GitHub Pages serves `scripts/index.html`;
- the API request is not blocked by a network filter.

## Results contain no exact article text

Tavily returns search excerpts. Open the official URL and verify the full document and its effective date.
