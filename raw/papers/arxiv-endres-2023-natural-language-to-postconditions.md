---
title: Can Large Language Models Transform Natural Language Intent into Formal Method Postconditions?
author: Madeline Endres, Sarah Fakhoury, Saikat Chakraborty, Shuvendu K. Lahiri
url: https://arxiv.org/abs/2310.01831v2
date: 2023-10-03
ingested: 2026-04-08
---

# Can Large Language Models Transform Natural Language Intent into Formal Method Postconditions?

**Source:** [arXiv](https://arxiv.org/abs/2310.01831v2)
**Authors:** Madeline Endres, Sarah Fakhoury, Saikat Chakraborty, Shuvendu K. Lahiri
**Date:** 2023-10-03
**Primary category:** cs.SE
**All categories:** cs.SE, cs.AI, cs.PL

## Abstract
Informal natural language that describes code functionality, such as code comments or function documentation, may contain substantial information about a programs intent. However, there is typically no guarantee that a programs implementation and natural language documentation are aligned. In the case of a conflict, leveraging information in code-adjacent natural language has the potential to enhance fault localization, debugging, and code trustworthiness. In practice, however, this information is often underutilized due to the inherent ambiguity of natural language which makes natural language intent challenging to check programmatically. The emergent abilities of Large Language Models (LLMs) have the potential to facilitate the translation of natural language intent to programmatically checkable assertions. However, it is unclear if LLMs can correctly translate informal natural language specifications into formal specifications that match programmer intent. Additionally, it is unclear if such translation could be useful in practice. In this paper, we describe nl2postcond, the problem of leveraging LLMs for transforming informal natural language to formal method postconditions, expressed as program assertions. We introduce and validate metrics to measure and compare different nl2postcond approaches, using the correctness and discriminative power of generated postconditions. We then use qualitative and quantitative methods to assess the quality of nl2postcond postconditions, finding that they are generally correct and able to discriminate incorrect code. Finally, we find that nl2postcond via LLMs has the potential to be helpful in practice; nl2postcond generated postconditions were able to catch 64 real-world historical bugs from Defects4J.
