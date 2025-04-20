# 🧱 WHO is SHE — TIER: 1–4 NFT (ARCHITECTURE LOCK)

This file documents the architectural specification for the 1–4 NFT tier.  
This tier gives users access to all currently minted stories (up to N = 
minted count).

---

### 🧩 Story Source

- All stories are stored as `.txt` files in:

arts/1to4_NFT_EN/01.txt ... {minted}.txt

- File count = number of minted NFTs
- Each file is loaded using the unified `get_story_text()` method

---

### 🧩 Image Source

- Images are served via GitHub Pages:

https://callmeshe.github.io/she-telegram-bot/arts/1to4_NFT_EN/{num}.jpg

---

### 🔐 Logic

- File access is restricted by verified wallet (ETH)
- Wallets with 1–4 NFTs get access to all currently minted stories
- The `MINTED_COUNT` is synced from a Google Sheet managed by the creator

---

### 🧪 Verification

- `telegram-bot-check.py` supports checking up to `MINTED_COUNT` files
- Run with tier parameter:

```bash
python3 telegram-bot-check.py --tier 1to4_NFT_EN

