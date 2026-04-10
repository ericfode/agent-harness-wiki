---
title: "Measuring Coding Challenge Competence With APPS"
author: "Dan Hendrycks, Steven Basart, Saurav Kadavath, Mantas Mazeika, Akul Arora, Ethan Guo, Collin Burns, Samir Puranik, Horace He, Dawn Song, Jacob Steinhardt"
url: https://arxiv.org/abs/2105.09938v3
date: 2021-05-20
ingested: 2026-04-10
---

# Measuring Coding Challenge Competence With APPS

**Source:** [arXiv](https://arxiv.org/abs/2105.09938v3)
**Authors:** Dan Hendrycks, Steven Basart, Saurav Kadavath, Mantas Mazeika, Akul Arora, Ethan Guo, Collin Burns, Samir Puranik, Horace He, Dawn Song, Jacob Steinhardt
**Date:** 2021-05-20
**Primary category:** cs.SE
**All categories:** cs.SE, cs.CL, cs.LG

## Abstract
While programming is one of the most broadly applicable skills in modern society, modern machine learning models still cannot code solutions to basic problems. Despite its importance, there has been surprisingly little work on evaluating code generation, and it can be difficult to accurately assess code generation performance rigorously. To meet this challenge, we introduce APPS, a benchmark for code generation. Unlike prior work in more restricted settings, our benchmark measures the ability of models to take an arbitrary natural language specification and generate satisfactory Python code. Similar to how companies assess candidate software developers, we then evaluate models by checking their generated code on test cases. Our benchmark includes 10,000 problems, which range from having simple one-line solutions to being substantial algorithmic challenges. We fine-tune large language models on both GitHub and our training set, and we find that the prevalence of syntax errors is decreasing exponentially as models improve. Recent models such as GPT-Neo can pass approximately 20% of the test cases of introductory problems, so we find that machine learning models are now beginning to learn how to code. As the social significance of automatic code generation increases over the coming years, our benchmark can provide an important measure for tracking advancements.

## Why it matters here
Primary APPS paper. It matters because any claim that neural-native representations outperform token-code baselines eventually has to survive harder, multi-test execution benchmarks.
