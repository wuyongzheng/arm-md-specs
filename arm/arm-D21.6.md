## D21.6 Effect of access type on MPAM information

IBZNRF

See the following subsections:

- Translation table accesses.

- Granule Protection Table (GPT) accesses.

- Accesses by enhanced support for nested virtualization.

- AT* instructions.

- Unprivileged memory access instructions.

- Accesses by Statistical Profiling Extension.

## D21.6.1 Translation table accesses

RFYLGZ

Translation table walk accesses, including hardware updates of translation tables, for:

- Instruction fetches, use the same PARTID\_I field as their instruction fetch.
- Data accesses, use the same PARTID\_D field as their data access.

## D21.6.2 Granule Protection Table (GPT) accesses

RMFSPP

In MPAM for RME, Granule Protection Table (GPT) accesses for:

- Instruction fetches, use the same PARTID space, PARTID\_I, field, and PMG\_I field as their instruction fetch.
- Data accesses, use the same PARTID space, PARTID\_D field, and PMG\_D field as their data access.
- Atranslation table walk, use the same PARTID space, PARTID, and PMG as the translation table access.

## D21.6.3 Accesses by enhanced support for nested virtualization

RNFJPN

In an MPAM PE with FEAT\_NV2, when the Effective value of HCR\_EL2.{NV, NV2} is {1, 1}, MRS and MSR accesses to certain registers from EL1 are transformed to memory accesses. Those accesses, and translation table walks generated for those accesses, use MPAM2\_EL2.{PARTID\_D, PMG\_D}. See Support for nested virtualization.

## D21.6.4 AT* instructions

RRSNZD

Accesses to translation tables by AT* instructions are given the MPAM information specified for translation table accesses by a data load instruction that is issued from an IMPLEMENTATION DEFINED choice of:

- The Exception level that the AT* instruction was executed from.
- The Exception level that configures the translation regime targeted by the AT* instruction.

## D21.6.5 Unprivileged memory access instructions

RGPVVG

For unprivileged memory access instructions executed at ELx, the resulting memory system requests use the same MPAMlabels that are used for regular loads and stores at ELx.

## D21.6.6 Accesses by Statistical Profiling Extension

RCRJBB

An MPAM PE with FEAT\_SPE can be configured to record statistically sampled events into a Profiling Buffer in memory. The buffer is accessed through the owning translation regime. MPAM PARTID, PMG, and PARTID space for SPE writes to the Profiling Buffer must use the SPE owning Exception level MPAM data access values. For example, if the owning Exception level is EL2, the Profiling Buffer writes must be performed with MPAM2\_EL2.PARTID\_D, MPAM2\_EL2.PMG\_D, with MPAM\_NS or MPAM\_SP reflecting the owning Security state.

## D21.6.7 Accesses by Trace Buffer Extension

IMNMXW

APEwith FEAT\_TRBE can be configured to record trace data into a trace buffer in memory. The MPAM information used for these accesses depends on the operating mode of the Trace Buffer Unit. For more information, see:

- Accesses by Trace Buffer Extension.
- External mode and MPAM.