## Chapter 2 Introduction

A System Memory Management Unit (SMMU) performs a task that is analogous to that of an MMU in a PE, translating addresses for DMA requests from system I/O devices before the requests are passed into the system interconnect. It is active for DMA only. Traffic in the other direction, from the system or PE to the device, is managed by other means - for example, the PE MMUs.

Figure 2.1: System MMU in DMA traffic

<!-- image -->

Translation of DMA addresses might be performed for reasons of isolation or convenience.

To associate device traffic with translations and to differentiate different devices behind an SMMU, requests have an extra property, alongside address, read/write, permissions, to identify a stream. Different streams are logically associated with different devices and the SMMU can perform different translations or checks for each stream. In systems with exactly one client device served by an SMMU the concept still stands, but might have only one

stream.

Several SMMUs might exist within a system. An SMMU might translate traffic from just one device or a set of devices.

The SMMU supports two stages of translation in a similar way to PEs supporting the Virtualization Extensions [2]. Each stage of translation can be independently enabled. An incoming address is logically translated from V A to IPA in stage 1, then the IPA is input to stage 2 which translates the IPA to the output PA. Stage 1 is intended to be used by a software entity to provide isolation or translation to buffers within the entity, for example DMA isolation within an OS. Stage 2 is intended to be available in systems supporting the Virtualization Extensions and is intended to virtualize device DMA to guest VM address spaces. When both stage 1 and stage 2 are enabled, the translation configuration is called nested .