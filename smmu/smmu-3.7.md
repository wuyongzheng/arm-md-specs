## 3.7 Programming registers

The SMMU registers occupy a set of contiguous 64K pages of system address space that contain mechanisms for discovering capabilities and configuring pointers to in-memory structures and queues. After initialization, runtime access to the registers is generally limited to maintenance of the Command, Event and PRI queue pointers and interaction with the SMMU is performed using these in-memory queues.

Optional regions of IMPLEMENTATION DEFINED register space are supported in the memory map.

See section 6.1 Memory map for register definitions and layout.