---
title: "Performance Analysis and Characterization of Training Deep Learning Models on Mobile Devices"
author: "Jie Liu, Jiawen Liu, Wan Du, Dong Li"
url: https://arxiv.org/abs/1906.04278v2
date: 2019-06-10
ingested: 2026-04-10
---

# Performance Analysis and Characterization of Training Deep Learning Models on Mobile Devices

**Source:** [arXiv](https://arxiv.org/abs/1906.04278v2)
**Authors:** Jie Liu, Jiawen Liu, Wan Du, Dong Li
**Date:** 2019-06-10
**Primary category:** cs.LG
**All categories:** cs.LG, cs.PF, stat.ML

## Abstract
Training deep learning models on mobile devices recently becomes possible, because of increasing computation power on mobile hardware and the advantages of enabling high user experiences. Most of the existing work on machine learning at mobile devices is focused on the inference of deep learning models (particularly convolutional neural network and recurrent neural network), but not training. The performance characterization of training deep learning models on mobile devices is largely unexplored, although understanding the performance characterization is critical for designing and implementing deep learning models on mobile devices. In this paper, we perform a variety of experiments on a representative mobile device (the NVIDIA TX2) to study the performance of training deep learning models. We introduce a benchmark suite and tools to study performance of training deep learning models on mobile devices, from the perspectives of memory consumption, hardware utilization, and power consumption. The tools can correlate performance results with fine-grained operations in deep learning models, providing capabilities to capture performance variance and problems at a fine granularity. We reveal interesting performance problems and opportunities, including under-utilization of heterogeneous hardware, large energy consumption of the memory, and high predictability of workload characterization. Based on the performance analysis, we suggest interesting research directions.

## Why it matters here
Primary structural-probe paper. It matters as both a measurement tool and a warning: it shows hidden structure can sometimes be linearly recovered, but not that such recovery defines the underlying computation.
