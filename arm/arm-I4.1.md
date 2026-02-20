## I4.1 About the external interface to the Activity Monitors Extension registers

If an implementation supports the Activity Monitors Extension, it can optionally support an external memory-mapped interface to the Activity Monitors Extension, FEAT\_AMU\_EXT. If the implementation supports FEAT\_AMU\_EXT, it may further optionally support CoreSight device registers and ID registers.

When FEAT\_AMU\_EXT64 is implemented, all AMU registers are 64-bit except the 32-bit CoreSight management registers, when implemented.

The base address of the memory-mapped view is aligned to a 4KB boundary, but is otherwise IMPLEMENTATION DEFINED. The address offsets for the memory-mapped view are given in Table I5-161.

When FEAT\_AMU\_EXT32 is implemented, AMCNTENSET0, AMCNTENSET1, AMCNTENCLR0, and AMCNTENCLR1are all read-only views of the 32-bit AMU count enable and disable control registers.

When FEAT\_AMU\_EXT64 is implemented, all of the following apply:

- AMCNTENSET0 and AMCNTENSET1 are accessed as a single 64-bit register, AMCNTENSET. AMCNTENSET[31:0] is architecturally mapped to AMCNTENSET0\_EL0[31:0] and AMCNTENSET[63:32] is architecturally mapped to AMCNTENSET1\_EL0[31:0].
- AMCNTENCLR0and AMCNTENCLR1 are accessed as a single 64-bit register AMCNTENCLR. AMCNTENCLR[31:0] is architecturally mapped to AMCNTENCLR0\_EL0[31:0], and AMCNTENCLR[63:32] is architecturally mapped to AMCNTENCLR1\_EL0[31:0].
- AMCNTENis provided as a 64-bit register, accessing the same state as the 64-bit AMU count enable and disable control registers, AMCNTENSET and AMCNTENCLR. This means that AMCNTEN, AMCNTENSET, and AMCNTENCLRare all read-only views of the same state.
- AMDEVAFF0 and AMDEVAFF1 are accessed as a single 64-bit register, AMDEVAFF.

## I4.1.1 Endianness and supported access sizes

In the external interface to the Activity Monitors, all registers are little endian.

Permitted accesses to the external interface to the Activity Monitors:

- Comply with the requirements of Supported access sizes.
- When FEAT\_AMU\_EXT32 is implemented, support word-aligned 32-bit accesses to access 32-bit registers or either half of a 64-bit register, even if all components with direct memory access to the AMU support making 64-bit accesses.

Permitted word-aligned 32-bit accesses are single-copy atomic at word granularity. When FEAT\_AMU\_EXT64 is implemented, permitted doubleword-aligned 64-bit accesses are single-copy atomic at doubleword granularity.

## I4.1.2 Differences in the external views of the Activity Monitors Extension registers

The external memory-mapped interface view of the Activity Monitors Extension registers accesses the same registers as the System registers interface to the registers, except that:

- The following are accessible only in the System registers interface:
- -AMUSERENR\_EL0.
- -AMEVCNTVOFF0&lt;n&gt;\_EL2.
- -AMEVCNTVOFF1&lt;n&gt;\_EL2.
- -AMCG1IDR\_EL0.
- If implemented, the following registers are accessible only in the memory-mapped view:
- -AMIIDR.
- -AMDEVAFF.
- -AMDEVAFF0.
- -AMDEVAFF1.
- -AMDEVARCH.
- -AMDEVTYPE.

Recommended External Interface to the Activity Monitors I4.1 About the external interface to the Activity Monitors Extension registers

- [ ] - AMPIDR0.

- [ ] - AMPIDR1.

- [ ] - AMPIDR2.

- [ ] - AMPIDR3.

- [ ] - AMPIDR4.

- [ ] - AMCIDR0.

- [ ] - AMCIDR1.

- [ ] - AMCIDR2.

- [ ] - AMCIDR3.

Activity Monitors external register descriptions describes these registers.

- If FEAT\_AMUv1p1 virtualization of the activity monitors is enabled, the memory-mapped view of the registers presents the physical view of the counter without any offset. Virtualization of the Activity Monitors does not affect the memory-mapped view of the registers.

Note

The memory mapped view of the activity monitors is unaffected byAMCR\_EL0.CG1RZ and AMCR.CG1RZ.

## I4.1.3 Access during reset and power transitions

As described in Power and reset domains, the power and reset domains of the Activity Monitoring Unit are named the AMUdomain and AMU reset, and when reset of the AMU power domain occurs, the Activity Monitoring Unit is reset and the counters are reset to zero.

If the AMU domain is an always-on power domain, while the PE is reset or powered down counter values may be preserved and might be accessible by memory-mapped access.

If the AMU domain is the Core power domain, while the PE is reset or powered down and when a memory-mapped access occurs, the access reads as zero and the bus access completes without an error.

## Chapter I5 External System Control Register Descriptions

This chapter describes the external system control registers. It excludes the External debug registers that are described in External Debug Register Descriptions. It contains the following sections:

- About the external system control register descriptions.
- External Performance Monitors registers summary.
- Performance Monitors external register descriptions.
- External Activity Monitors Extension registers summary.
- Activity Monitors external register descriptions.
- Generic Timer memory-mapped registers overview.
- Generic Timer memory-mapped register descriptions.