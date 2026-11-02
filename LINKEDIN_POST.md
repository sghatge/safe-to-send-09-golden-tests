Safe to Send · Ep 09 — Tests before models

Before adding an AI model to my CRM rules, I froze what the rules decide today.

It's called a golden test: run every case once, save the verdicts, commit the file. From then on, any change that moves a verdict fails loudly and shows exactly which case moved.

Then I made two "harmless" config edits: subject limit 50 → 60, send window 21:00 → 22:00.

The golden test failed and named two markets:
→ Greece: a 21:30 send went from blocked to allowed
→ Hungary: a long subject went from blocked to allowed

Nobody touched a model, yet two market outcomes changed. Imagine debugging that after you've also added an LLM.

Boring, 40 lines, and it's how I can tell whether the model or the rules caused a change.

Repo: https://github.com/sghatge/safe-to-send-09-golden-tests

#SafeToSend #Testing #AIEngineering
