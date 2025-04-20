# 🛡 WHO is SHE — SECURITY RULES

These are the architectural and editorial constraints that must be 
enforced across the entire project.

---

## ❌ Forbidden in production

The following patterns are **not allowed** in any tier or version:

- HARDCODED_STORIES or fallback dictionaries
- add_default_stories(), get_story_content(), or similar mechanisms
- Substitution logic like:

```python
if not story_text:
    story_text = fallback[num]

