## A2.3 Armv9-A architecture extensions

The AArch32 state might optionally be implemented at EL0. The AArch32 state is not implemented at EL1, EL2, and EL3.

The implementation of FEAT\_DoubleLock in an Armv9 implementation is prohibited.

An implementation of the Armv9-A architecture cannot include an ETM.

## A2.3.1 The Armv9.0 architecture extension

The Armv9.0 architecture extension adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv9.0 compliant if all of the following apply:

- It is Armv8.5 compliant.
- It includes all of the Armv9.0 architectural features that are mandatory.

An Armv9.0 compliant implementation can additionally include:

- Armv9.0 features that are optional.
- Any arbitrary subset of the architectural features of Armv9.1, subject only to those constraints that require that certain features be implemented together.

In an Armv9.0 implementation, the AArch32 state might optionally be implemented at EL0. The AArch32 state is not implemented at EL1, EL2, and EL3.

An implementation of Armv9.0 cannot implement FEAT\_DoubleLock.

An implementation of the Armv9.0 architecture cannot include an ETM.

In an Armv9.0 implementation, if FEAT\_FP and FEAT\_AdvSIMD are implemented, the following features are implemented:

- FEAT\_RDM.
- FEAT\_FP16.
- FEAT\_DotProd.
- FEAT\_FHM.
- FEAT\_FCMA.
- FEAT\_JSCVT.
- FEAT\_FlagM2.
- FEAT\_FRINTTS.

## FEAT\_Armv9\_Crypto, Armv9 Cryptographic Extension

The Armv9 Cryptographic Extension provides instructions for the acceleration of encryption and decryption. The presence of the Cryptographic Extension in an implementation is subject to export license controls.

This feature is supported in AArch64 state only.

FEAT\_Armv9\_Crypto is OPTIONAL.

If FEAT\_Armv9\_Crypto is implemented, then FEAT\_Crypto is implemented.

If FEAT\_Armv9\_Crypto is implemented, then FEAT\_PMULL, FEAT\_AES, FEAT\_SHA1, FEAT\_SHA3, FEAT\_SHA256, and FEAT\_SHA512 are implemented.

When FEAT\_Armv9\_Crypto, FEAT\_SVE and FEAT\_SVE\_SHA3 are implemented, FEAT\_SVE\_AES, and FEAT\_SVE\_PMULL128 are implemented.

When FEAT\_Armv9\_Crypto, FEAT\_SVE and FEAT\_SVE\_AES are implemented, FEAT\_SVE\_PMULL128, and FEAT\_SVE\_SHA3 are implemented.

When FEAT\_Armv9\_Crypto, FEAT\_SVE and FEAT\_SVE\_PMULL128 are implemented, FEAT\_SVE\_AES, and FEAT\_SVE\_SHA3 are implemented.

For more information, see:

- The Cryptographic Extension in AArch64 state.
- The Cryptographic Extension in AArch32 state.

## FEAT\_ETE, Embedded Trace Extension

FEAT\_ETE provides a trace unit that records details about software control flow running on a PE, which can be used to aid debugging or optimizing. The trace unit provides filtering functionality to allow the targeting of the information to specific code regions or periods of operation.

This feature is supported in AArch64 state, and performs trace in both AArch64 and AArch32 states.

FEAT\_ETE is OPTIONAL from Armv9.0.

If FEAT\_ETE is implemented, then FEAT\_TRBE is implemented.

If FEAT\_ETE is implemented, then FEAT\_TRF is implemented.

If FEAT\_ETE is implemented, then FEAT\_TRC\_SR is implemented.

If FEAT\_ETE is implemented, then FEAT\_ETMv4 is not implemented.

When FEAT\_ETE and FEAT\_PMUv3 are implemented, FEAT\_PMUv3p1 is implemented.

For more information, see The Embedded Trace Extension.

## FEAT\_SVE2, Scalable Vector Extension version 2

The Scalable Vector Extension version 2 (SVE2) is a superset of SVE that incorporates functionality similar to Advanced SIMD, and other enhancements. In this Manual, unless stated otherwise, when SVE is used, the behavior also applies to SVE2. All Armv9-A systems that support standard operating systems with rich application environments also provide hardware support for SVE2 instructions.

This feature is supported in AArch64 state only.

FEAT\_SVE2 is OPTIONAL from Armv9.0.

If FEAT\_SVE2 is implemented, then FEAT\_SVE is implemented.

The following field identifies the presence of FEAT\_SVE2:

- ID\_AA64ZFR0\_EL1.SVEver.

For more information, see:

- FEAT\_SVE.
- Data processing - SVE2.

## FEAT\_SVE\_AES, Scalable Vector AES instructions

FEAT\_SVE\_AES provides the following scalable vector AES cryptographic instructions:

- AESD.
- AESE.
- AESIMC.
- AESMC.
- PMULLB.
- PMULLT.

This feature is supported in AArch64 state only.

FEAT\_SVE\_AES is OPTIONAL from Armv9.0.

If FEAT\_SVE\_AES is implemented, then FEAT\_SVE2 or FEAT\_SSVE\_AES is implemented.

If FEAT\_SVE\_AES is implemented, then FEAT\_SVE\_PMULL128 is implemented.

If FEAT\_SVE\_PMULL128 is implemented, then FEAT\_SVE\_AES is implemented.

If FEAT\_SVE\_AES is implemented, then FEAT\_Armv9\_Crypto is implemented.

The following field identifies the presence of FEAT\_SVE\_AES:

- ID\_AA64ZFR0\_EL1.AES.

## FEAT\_SVE\_BitPerm, Scalable Vector Bit Permutes instructions

FEAT\_SVE\_BitPerm provides the following scalable vector bit permute instructions:

- BEXT.
- BDEP.
- BGRP.

This feature is supported in AArch64 state only.

FEAT\_SVE\_BitPerm is OPTIONAL from Armv9.0.

If FEAT\_SVE\_BitPerm is implemented, then FEAT\_SVE2 is implemented.

The following field identifies the presence of FEAT\_SVE\_BitPerm:

- ID\_AA64ZFR0\_EL1.BitPerm.

For more information, see:

- 'Bit permutation'.

## FEAT\_SVE\_PMULL128, SVE single-vector Advanced Encryption Standard and 128-bit polynomial multiply long instructions

FEAT\_SVE\_PMULL128 implements the SVE single-vector Advanced Encryption Standard and 128-bit destination element variants of PMULLB and PMULLT instructions, when the PE is not in Streaming SVE mode.

This feature is supported in AArch64 state only.

FEAT\_SVE\_PMULL128 is OPTIONAL from Armv9.0.

If FEAT\_SVE\_PMULL128 is implemented, then FEAT\_SVE2 or FEAT\_SSVE\_AES is implemented.

If FEAT\_SVE\_PMULL128 is implemented, then FEAT\_SVE\_AES is implemented.

The following field identifies the presence of FEAT\_SVE\_PMULL128:

- ID\_AA64ZFR0\_EL1.AES.

## FEAT\_SVE\_SHA3, Scalable Vector SHA3 instructions

FEAT\_SVE\_SHA3 provides the following scalable vector SHA3 instruction:

- RAX1.

This feature is supported in AArch64 state only.

FEAT\_SVE\_SHA3 is OPTIONAL from Armv9.0.

If FEAT\_SVE\_SHA3 is implemented, then FEAT\_SVE2 or FEAT\_SME2p1 is implemented.

If FEAT\_SVE\_SHA3 is implemented, then FEAT\_Armv9\_Crypto is implemented.

The following field identifies the presence of FEAT\_SVE\_SHA3:

- ID\_AA64ZFR0\_EL1.SHA3.

## FEAT\_SVE\_SM4, Scalable Vector SM4 instructions

FEAT\_SVE\_SM4 provides the following scalable vector SM4 instructions:

- SM4E.
- SM4EKEY.

This feature is supported in AArch64 state only.

FEAT\_SVE\_SM4 is OPTIONAL from Armv9.0.

If FEAT\_SVE\_SM4 is implemented, then FEAT\_SVE2 is implemented.

If FEAT\_SVE\_SM4 is implemented, then FEAT\_SM4 is implemented.

The following field identifies the presence of FEAT\_SVE\_SM4:

- ID\_AA64ZFR0\_EL1.SM4.

## FEAT\_TRBE, Trace Buffer Extension

FEAT\_TRBE enables support for a Trace Buffer Unit within a PE. When the Trace Buffer Unit is enabled, program-flow trace generated by a trace unit is written directly to memory by the Trace Buffer Unit, rather than routing trace data to a trace sink.

This feature is supported in AArch64 state, and collects trace in both AArch64 and AArch32 states.

FEAT\_TRBE is OPTIONAL from Armv9.0.

If FEAT\_TRBE is implemented, then FEAT\_TRF is implemented.

If FEAT\_TRBE is implemented, then FEAT\_ETE is implemented.

When FEAT\_TRBE and FEAT\_PMUv3 are implemented, FEAT\_PMUv3p1 is implemented.

The following field identifies the presence of FEAT\_TRBE:

- ID\_AA64DFR0\_EL1.TraceBuffer.

For more information, see The Trace Buffer Extension.

## A2.3.1.1 Features added to the Armv9.0 extension in later releases

- FEAT\_IDTE3.
- FEAT\_PCDPHINT.
- FEAT\_UINJ.

## A2.3.2 The Armv9.1 architecture extension

The Armv9.1 architecture extension is an extension to Armv9.0. It adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv9.1 compliant if all of the following apply:

- It is Armv8.6 compliant.
- It is Armv9.0 compliant.
- It includes all of the Armv9.1 architectural features that are mandatory.

An Armv9.1 compliant implementation can additionally include:

- Armv9.1 features that are optional.
- Any arbitrary subset of the architectural features of Armv9.2, subject only to those constraints that require that certain features be implemented together.

## FEAT\_ETEv1p1, Embedded Trace Extension

FEAT\_ETEv1p1 extends FEAT\_ETE to provide more flexibility for tracing Timestamp values.

This feature is supported in AArch64 state, and performs trace in both AArch64 and AArch32 states.

FEAT\_ETEv1p1 is OPTIONAL from Armv9.0.

If FEAT\_ETEv1p1 is implemented, then FEAT\_ETE is implemented.

The following fields identify the presence of FEAT\_ETEv1p1:

- TRCDEVARCH.REVISION.
- TRCDEVARCH.REVISION.

For more information, see The Embedded Trace Extension..

## A2.3.3 The Armv9.2 architecture extension

The Armv9.2 architecture extension is an extension to Armv9.1. It adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv9.2 compliant if all of the following apply:

- It is Armv8.7 compliant.
- It is Armv9.1 compliant.
- It includes all of the Armv9.2 architectural features that are mandatory.

An Armv9.2 compliant implementation can additionally include:

- Armv9.2 features that are optional.
- Any arbitrary subset of the architectural features of Armv9.3, subject only to those constraints that require that certain features be implemented together.

## FEAT\_BRBE, Branch Record Buffer Extension

FEAT\_BRBE provides a Branch record buffer for capturing control path history.

This feature is supported in AArch64 state only.

FEAT\_BRBE is OPTIONAL from Armv9.1.

The following field identifies the presence of FEAT\_BRBE:

- ID\_AA64DFR0\_EL1.BRBE.

For more information, see The Branch Record Buffer Extension.

## FEAT\_ETEv1p2, Embedded Trace Extension

FEAT\_ETEv1p2 extends FEAT\_ETE to support FEAT\_RME.

This feature is supported in AArch64 state, and performs trace in both AArch64 and AArch32 states.

FEAT\_ETEv1p2 is OPTIONAL from Armv9.1.

If FEAT\_ETEv1p2 is implemented, then FEAT\_ETEv1p1 is implemented.

If FEAT\_ETE and FEAT\_RME are implemented, then FEAT\_ETEv1p2 is implemented.

The following fields identify the presence of FEAT\_ETEv1p2:

- TRCDEVARCH.REVISION.
- TRCDEVARCH.REVISION.

For more information, see The Embedded Trace Extension..

## FEAT\_RME, Realm Management Extension

The Realm Management Extension (RME) is an extension to the Armv9 A-profile architecture.

RMEintroduces all of the following features:

- Two additional Security states, Root and Realm.
- Two additional physical address spaces, Root and Realm.
- The ability to dynamically transition memory granules between physical address spaces.
- Granule Protection Check mechanism.

FEAT\_RME is one component of the Arm Confidential Compute Architecture (Arm CCA). Together with the other components of the Arm CCA, RME enables support for dynamic, attestable, and trusted execution environments (Realms) to be run on an Arm PE.

This feature is supported in AArch64 state only.

FEAT\_RME is OPTIONAL from Armv9.1.

If FEAT\_RME is implemented, then FEAT\_AA64EL3, FEAT\_AA64EL2, and FEAT\_RNG or FEAT\_RNG\_TRAP are implemented.

When FEAT\_RME and FEAT\_AES or FEAT\_SHA1 are implemented, FEAT\_PMULL, FEAT\_AES, FEAT\_SHA3, FEAT\_SHA256, and FEAT\_SHA512 are implemented.

When FEAT\_RME, FEAT\_SVE and FEAT\_AES or FEAT\_SHA1 are implemented, FEAT\_SVE\_PMULL128, and FEAT\_SVE\_SHA3 are implemented.

When FEAT\_ETE and FEAT\_RME are implemented, FEAT\_ETEv1p2 is implemented.

When FEAT\_PMUv3 and FEAT\_RME are implemented, FEAT\_PMUv3p7 is implemented.

When FEAT\_SPE and FEAT\_RME are implemented, FEAT\_SPEv1p2 is implemented.

When FEAT\_MPAM and FEAT\_RME are implemented, FEAT\_MPAMv1p1 is implemented.

If FEAT\_RME is implemented, then FEAT\_PCSRv8 is not implemented.

The following field identifies the presence of FEAT\_RME:

- ID\_AA64PFR0\_EL1.RME.

If the Activity Monitors Extension is implemented, then Arm strongly recommends that a PE that implements FEAT\_RME also implements FEAT\_AMUv1p1.

Arm recommends that a PE that implements FEAT\_RME also implements all of the following:

- FEAT\_VMID16.
- FEAT\_HAFDBS.

For more information, see:

- The AArch64 System Level Programmers´ Model.
- The AArch64 Virtual Memory System Architecture.
- The Granule Protection Check Mechanism.

## FEAT\_SME, Scalable Matrix Extension

FEAT\_SME introduces two AArch64 execution modes that can be enabled and disabled by application software:

- In ZA storage enabled mode, scalable, two-dimensional, architectural ZA tile storage becomes available and instructions are defined to load, store, extract, insert, and clear rows and columns of the ZA tiles.
- In Streaming SVE mode, the Effective SVE vector length changes to match the Effective ZA tile width, support for a substantial subset of the SVE2 instruction set is available, and, when ZA mode is also enabled, instructions are defined that accumulate the matrix outer product of two SVE vectors into a ZA tile.

This feature is supported in AArch64 state only.

FEAT\_SME is OPTIONAL from Armv9.2.

If FEAT\_SME is implemented, then FEAT\_FCMA, FEAT\_FP16, FEAT\_BF16, and FEAT\_FHM are implemented.

When FEAT\_SME and FEAT\_EL2 are implemented, FEAT\_FGT and FEAT\_HCX are implemented.

When FEAT\_SME and FEAT\_PMUv3 are implemented, FEAT\_PMUv3p1 is implemented.

The following fields identify the presence of FEAT\_SME:

- ID\_AA64PFR1\_EL1.SME.
- ID\_AA64SMFR0\_EL1.F16F32.
- ID\_AA64SMFR0\_EL1.B16F32.
- ID\_AA64SMFR0\_EL1.F32F32.
- ID\_AA64SMFR0\_EL1.I8I32.

If FEAT\_SME is implemented, this does not imply that FEAT\_SVE and FEAT\_SVE2 are implemented when the PE is not in Streaming SVE mode.

For more information, see The Scalable Matrix Extension.

## FEAT\_SME\_F64F64, Double-precision floating-point outer product instructions

FEAT\_SME\_F64F64 indicates SME support for instructions that accumulate into double-precision floating-point elements in the ZA array.

This feature is supported in AArch64 state only.

FEAT\_SME\_F64F64 is OPTIONAL from Armv9.2.

If FEAT\_SME\_F64F64 is implemented, then FEAT\_SME is implemented.

The following field identifies the presence of FEAT\_SME\_F64F64:

- ID\_AA64SMFR0\_EL1.F64F64.

For more information, see The Scalable Matrix Extension.

## FEAT\_SME\_FA64, Full A64 instruction set support in Streaming SVE mode

FEAT\_SME\_FA64 indicates support for execution of the full A64 instruction set in Streaming SVE mode.

This feature is supported in AArch64 state only.

FEAT\_SME\_FA64 is OPTIONAL from Armv9.2.

If FEAT\_SME\_FA64 is implemented, then FEAT\_SME is implemented.

If FEAT\_SME\_FA64 is implemented, then FEAT\_SVE2 is implemented.

The following field identifies the presence of FEAT\_SME\_FA64:

- ID\_AA64SMFR0\_EL1.FA64.

For more information, see The Scalable Matrix Extension.

## FEAT\_SME\_I16I64, 16-bit to 64-bit integer widening outer product instructions

FEAT\_SME\_I16I64 indicates SME support for instructions that accumulate into 64-bit integer elements in the ZA array.

This feature is supported in AArch64 state only.

FEAT\_SME\_I16I64 is OPTIONAL from Armv9.2.

If FEAT\_SME\_I16I64 is implemented, then FEAT\_SME is implemented.

The following field identifies the presence of FEAT\_SME\_I16I64:

- ID\_AA64SMFR0\_EL1.I16I64.

For more information, see The Scalable Matrix Extension.

## A2.3.3.1 Features added to the Armv9.2 extension in later releases

- FEAT\_F8F16MM.
- FEAT\_F8F32MM.
- FEAT\_FAMINMAX.
- FEAT\_FP8DOT2.
- FEAT\_FP8DOT4.
- FEAT\_FP8FMA.
- FEAT\_FP8.
- FEAT\_FPMR.
- FEAT\_LS64WB.
- FEAT\_LUT.
- FEAT\_SME2p1.
- FEAT\_SME\_B16B16.
- FEAT\_SME\_F16F16.
- FEAT\_SME\_F8F16.
- FEAT\_SME\_F8F32.
- FEAT\_SME\_LUTv2.
- FEAT\_SPE\_SME.
- FEAT\_SSVE\_FP8DOT2.
- FEAT\_SSVE\_FP8DOT4.
- FEAT\_SSVE\_FP8FMA.
- FEAT\_SVE2p1.
- FEAT\_SVE\_B16B16.
- FEAT\_SVE\_BFSCALE.
- FEAT\_SVE\_F16F32MM.

## A2.3.4 The Armv9.3 architecture extension

The Armv9.3 architecture extension is an extension to Armv9.2. It adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv9.3 compliant if all of the following apply:

- It is Armv8.8 compliant.
- It is Armv9.2 compliant.
- It includes all of the Armv9.3 architectural features that are mandatory.

An Armv9.3 compliant implementation can additionally include:

- Armv9.3 features that are optional.
- Any arbitrary subset of the architectural features of Armv9.4, subject only to those constraints that require that certain features be implemented together.

## FEAT\_BRBEv1p1, Branch Record Buffer Extension version 1.1

FEAT\_BRBEv1p1 extends FEAT\_BRBE to enable branch recording at EL3.

This feature is supported in AArch64 state only.

FEAT\_BRBEv1p1 is OPTIONAL from Armv9.2.

In an Armv9.3 implementation, if FEAT\_BRBE is implemented, FEAT\_BRBEv1p1 is implemented.

If FEAT\_BRBEv1p1 is implemented, then FEAT\_BRBE is implemented.

The following field identifies the presence of FEAT\_BRBEv1p1:

- ID\_AA64DFR0\_EL1.BRBE.

For more information, see The Branch Record Buffer Extension.

## FEAT\_MEC, Memory Encryption Contexts

Memory Encryption Contexts (MEC) is an extension to the RME.

An existing RME enabled system uses a combination of isolation and external memory protection to guarantee privacy of the Realm Security state. Isolation between Realms is enforced by the Realm stage 2 translation tables.

FEAT\_MEC introduces all of the following features:

- Memory encryption contexts are provided to all physical address spaces.
- Multiple memory encryption contexts are provided to the Realm physical address space for assignment to Realm virtual machines, with policy controlled by Realm EL2.
- The Non-secure, Secure, and Root, physical address spaces each have one encryption context.

This feature is supported in AArch64 state only.

FEAT\_MEC is OPTIONAL from Armv9.2.

If FEAT\_MEC is implemented, then FEAT\_RME is implemented.

If FEAT\_MEC is implemented, then FEAT\_SCTLR2 is implemented.

If FEAT\_MEC is implemented, then FEAT\_TCR2 is implemented.

The following field identifies the presence of FEAT\_MEC:

- ID\_AA64MMFR3\_EL1.MEC.

## FEAT\_SME2, Scalable Matrix Extensions version 2

FEAT\_SME2 is a superset of FEAT\_SME that introduces the following:

- The ability to treat the SME ZA array as containing addressable groups of one-dimensional ZA array vectors, instead of two-dimensional ZA tiles.
- Multi-vector instructions that operate on groups of Z vector registers and ZA array vectors.
- Amulti-vector predication mechanism for multi-vector load and store.
- Adedicated 512-bit lookup table register, ZT0, for data decompression.

This feature is supported in AArch64 state only.

FEAT\_SME2 is OPTIONAL from Armv9.2.

If FEAT\_SME2 is implemented, then FEAT\_SME is implemented.

The following fields identify the presence of FEAT\_SME2:

- ID\_AA64SMFR0\_EL1.SMEver.
- ID\_AA64PFR1\_EL1.SME.
- ID\_AA64SMFR0\_EL1.BI32I32.
- ID\_AA64SMFR0\_EL1.I16I32.

For more information, see The Scalable Matrix Extension.

## A2.3.4.1 Features added to the Armv9.3 extension in later releases

- FEAT\_LSFE.
- FEAT\_MPAM\_PE\_BW\_CTRL.
- FEAT\_OCCMO.

## A2.3.5 The Armv9.4 architecture extension

The Armv9.4 architecture extension is an extension to Armv9.3. It adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv9.4 compliant if all of the following apply:

- It is Armv8.9 compliant.
- It is Armv9.3 compliant.
- It includes all of the Armv9.4 architectural features that are mandatory.

An Armv9.4 compliant implementation can additionally include:

- Armv9.4 features that are optional.

## FEAT\_ABLE, Address Breakpoint Linking Extension

FEAT\_ABLE introduces the capability to link a watchpoint to an address matching breakpoint.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_ABLE is OPTIONAL from Armv9.3.

If FEAT\_ABLE is implemented, then FEAT\_BWE is implemented.

If FEAT\_ABLE is implemented, then FEAT\_Debugv8p9 is implemented.

The following fields identify the presence of FEAT\_ABLE:

- ID\_AA64DFR1\_EL1.ABLE.
- EDDFR1.ABLE.

For more information, see About Breakpoint exceptions.

## FEAT\_BWE, Breakpoint and watchpoint enhancements

FEAT\_BWE introduces the capability to define an included-range-based breakpoint and an excluded-range-based breakpoint.

This feature is supported in AArch64 state only.

FEAT\_BWE is OPTIONAL from Armv9.3.

The following fields identify the presence of FEAT\_BWE:

- ID\_AA64DFR2\_EL1.BWE.
- ID\_AA64DFR1\_EL1.ABLE.
- EDDFR1.ABLE.
- EDDFR2.BWE.

For more information, see Other usage constraints for Address breakpoints.

## FEAT\_CHK, Check Feature Status

FEAT\_CHK introduces the CHKFEAT instruction, which allows software to detect when certain features are enabled.

APEthat is compliant with architectures from Armv8.0 to Armv9.3 is compliant with the behavior defined for this feature.

This feature is supported in AArch64 state only.

FEAT\_CHK is OPTIONAL from Armv8.0.

FEAT\_CHK is mandatory from Armv9.4.

For more information, see Detecting when FEAT\_GCS is enabled.

## FEAT\_D128, 128-bit Translation Tables, 56 bit PA

FEAT\_D128 introduces support for the VMSAv9-128 translation system, comprising the following:

- 128-bit translation table descriptors.
- Support for encoding up to 56-bit physical addresses in translation table descriptors.
- If FEAT\_LVA or FEAT\_LVA3 are implemented, support for translating up to 56-bit virtual addresses.
- TLBIP VA , TLBIP RVA , TLBIP IPA , TLBIP RIPA instructions that can take 128-bit inputs.

This feature is supported in AArch64 state only.

FEAT\_D128 is OPTIONAL from Armv9.3.

If FEAT\_D128 is implemented, then FEAT\_SYSREG128 is implemented.

If FEAT\_D128 is implemented, then FEAT\_SYSINSTR128 is implemented.

If FEAT\_D128 is implemented, then FEAT\_LSE128 is implemented.

If FEAT\_D128 is implemented, then FEAT\_S1PIE is implemented.

When FEAT\_D128 and FEAT\_EL2 are implemented, FEAT\_S2PIE is implemented.

If FEAT\_D128 is implemented, then FEAT\_AIE is implemented.

If FEAT\_D128 is implemented, then FEAT\_TCR2 is implemented.

The following field identifies the presence of FEAT\_D128:

- ID\_AA64MMFR3\_EL1.D128.

For more information, see The AArch64 Virtual Memory System Architecture.

## FEAT\_EBEP, Exception-based Event Profiling

FEAT\_EBEP provides support for reporting PMU counter overflows as PMU Profiling exceptions. This allows generation of higher quality profiles by eliminating the interrupt latency and jitter incurred outside the PE.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_EBEP is OPTIONAL from Armv9.3.

In an Armv9.3 implementation, if FEAT\_PMUv3p9 is implemented, FEAT\_EBEP is implemented.

When FEAT\_EBEP and FEAT\_AA64EL2 are implemented, FEAT\_FGT2 is implemented.

When FEAT\_EBEP and FEAT\_AA32EL0 are implemented, FEAT\_Debugv8p9 is implemented.

The following field identifies the presence of FEAT\_EBEP:

- ID\_AA64DFR1\_EL1.EBEP.

For more information, see Exception-based event profiling.

## FEAT\_ETEv1p3, Embedded Trace Extension version 1.3

FEAT\_ETEv1p3 extends FEAT\_ETE to support all of the following:

- The ETE External Debug Request, when FEAT\_Debugv8p9 is implemented.
- The ETE Trace Output Enable, which is mandatory for FEAT\_ETEv1p3 and OPTIONAL for FEAT\_ETE.

This feature is supported in AArch64 state, and performs trace in both AArch64 and AArch32 states.

FEAT\_ETEv1p3 is OPTIONAL from Armv9.3.

If FEAT\_ETEv1p3 is implemented, then FEAT\_ETEv1p2 is implemented.

The following fields identify the presence of FEAT\_ETEv1p3:

- TRCDEVARCH.REVISION.
- TRCDEVARCH.REVISION.

For more information, see The Embedded Trace Extension.

## FEAT\_GCS, Guarded Control Stack Extension

FEAT\_GCS introduces support for a Guarded Control Stack, an area of memory in which procedure return addresses and exception return addresses are stored and protected from modification.

This feature is supported in AArch64 state only.

FEAT\_GCS is OPTIONAL from Armv9.3.

If FEAT\_GCS is implemented, then FEAT\_CHK is implemented.

If FEAT\_GCS is implemented, then FEAT\_S1PIE is implemented.

The following field identifies the presence of FEAT\_GCS:

- ID\_AA64PFR1\_EL1.GCS.

For more information, see Guarded Control Stack.

## FEAT\_ITE, Instrumentation Trace Extension

FEAT\_ITE provides all of the following to allow software to inject instrumentation information into the ETE trace stream:

- The TRCIT instruction, that injects the value of a general purpose register into the ETE trace stream.
- Instrumentation Packet that contains the value written by the TRCIT instruction.

- Controls that define the behavior of the TRCIT instruction.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_ITE is OPTIONAL from Armv9.3.

If FEAT\_ITE is implemented, then FEAT\_TRF is implemented.

If FEAT\_ITE is implemented, then FEAT\_ETE is implemented.

If FEAT\_ITE is implemented, then FEAT\_TRBE is implemented.

When FEAT\_ITE and FEAT\_AA64EL2 are implemented, FEAT\_FGT2 is implemented.

The following fields identify the presence of FEAT\_ITE:

- ID\_AA64DFR1\_EL1.ITE.
- TRCIDR0.ITE.
- TRCIDR0.ITE.

For more information, see:

- Instrumentation extension.
- Instrumentation element.

## FEAT\_LSE128, 128-bit Atomics

FEAT\_LSE128 introduces support for 128-bit atomic instructions.

This feature is supported in AArch64 state only.

FEAT\_LSE128 is OPTIONAL from Armv9.3.

If FEAT\_LSE128 is implemented, then FEAT\_LSE is implemented.

The following field identifies the presence of FEAT\_LSE128:

- ID\_AA64ISAR0\_EL1.Atomic.

For more information, see:

- Atomic integer memory operations.
- Swap operations.

## FEAT\_LVA3, 56-bit VA

FEAT\_LVA3 introduces support for 56-bit virtual addresses.

This feature is supported in AArch64 state only.

FEAT\_LVA3 is OPTIONAL from Armv9.3.

If FEAT\_LVA3 is implemented, then FEAT\_D128 is implemented.

If FEAT\_LVA3 is implemented, then FEAT\_LVA is implemented.

The following field identifies the presence of FEAT\_LV A3:

- ID\_AA64MMFR2\_EL1.VARange.

For more information, see Supported virtual address ranges.

## FEAT\_SEBEP, Synchronous Exception-based Event Profiling

FEAT\_SEBEP creates configurations to generate synchronous and precise PMU Profiling exceptions.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_SEBEP is OPTIONAL from Armv9.3.

If FEAT\_SEBEP is implemented, then FEAT\_EBEP is implemented.

When FEAT\_SEBEP and FEAT\_AA64EL2 are implemented, FEAT\_FGT2 is implemented.

When FEAT\_SEBEP and FEAT\_AA32EL0 are implemented, FEAT\_Debugv8p9 is implemented.

The following field identifies the presence of FEAT\_SEBEP:

- ID\_AA64DFR0\_EL1.SEBEP.

For more information, see:

- Synchronous exception-based event profiling.
- Synchronous events.

## FEAT\_SME2p1, Scalable Matrix Extension version 2.1

The Scalable Matrix Extension version 2.1 (SME2.1) is a superset of SME2 that adds:

- Support for SVE RAX1 instructions in Streaming SVE mode if FEAT\_SVE\_SHA3 is implemented.
- SMEMOVAZinstructions that move and zero ZA array vectors or ZA tile slices.
- SMEZEROinstructions that zero ZA array vectors.
- SMELUTI2 and LUTI4 lookup table instructions to Z vectors with strided numbering.

In this Manual, unless stated otherwise, when SME is used, the behavior also applies to SME2.1.

This feature is supported in AArch64 state only.

FEAT\_SME2p1 is OPTIONAL from Armv9.2.

In an Armv9.4 implementation, if FEAT\_SME2 is implemented, FEAT\_SME2p1 is implemented.

If FEAT\_SME2p1 is implemented, then FEAT\_SME2 is implemented.

If FEAT\_SME and FEAT\_SVE2p1 are implemented, then FEAT\_SME2p1 is implemented.

The following field identifies the presence of FEAT\_SME2p1:

- ID\_AA64SMFR0\_EL1.SMEver.

For more information, see:

- Data processing - SME, SME2.
- The Scalable Matrix Extension.

## FEAT\_SME\_B16B16, Non-widening BFloat16 to BFloat16 SME ZA-targeting arithmetic

FEAT\_SME\_B16B16 introduces SME ZA-targeting non-widening BFloat16 floating-point instructions to SME.

This feature is supported in AArch64 state only.

FEAT\_SME\_B16B16 is OPTIONAL from Armv9.2.

If FEAT\_SME\_B16B16 is implemented, then FEAT\_SME2 is implemented.

If FEAT\_SME\_B16B16 is implemented, then FEAT\_SVE\_B16B16 is implemented.

The following field identifies the presence of FEAT\_SME\_B16B16:

- ID\_AA64SMFR0\_EL1.B16B16.

## FEAT\_SME\_F16F16, Non-widening half-precision FP16 to FP16 arithmetic for SME2

FEAT\_SME\_F16F16 introduces the SME2 half-precision to single-precision convert instructions and non-widening half-precision floating-point instructions.

This feature is supported in AArch64 state only.

FEAT\_SME\_F16F16 is OPTIONAL from Armv9.2.

If FEAT\_SME\_F16F16 is implemented, then FEAT\_SME2 is implemented.

The following field identifies the presence of FEAT\_SME\_F16F16:

- ID\_AA64SMFR0\_EL1.F16F16.

For more information, see:

- Data processing - SME, SME2.
- The Scalable Matrix Extension.

## FEAT\_SVE2p1, Scalable Vector Extensions version 2.1

The Scalable Vector Extension version 2.1 (SVE2.1) is a superset of SVE2 that adds:

- SVE instructions in Non-streaming SVE mode, which were previously added by SME in Streaming SVE mode. These are:
- Contiguous multi-vector load and store instructions.
- Predicate-as-counter instructions.
- General-purpose SVE instructions.
- Other relaxations and enhancements.

In this Manual, unless stated otherwise, when SVE is used, the behavior also applies to SVE2.1.

This feature is supported in AArch64 state only.

FEAT\_SVE2p1 is OPTIONAL from Armv9.2.

In an Armv9.4 implementation, if FEAT\_SVE2 is implemented, FEAT\_SVE2p1 is implemented.

If FEAT\_SVE2p1 is implemented, then FEAT\_SVE2 is implemented.

If FEAT\_SVE2 and FEAT\_SME2p1 are implemented, then FEAT\_SVE2p1 is implemented.

The following field identifies the presence of FEAT\_SVE2p1:

- ID\_AA64ZFR0\_EL1.SVEver.

For more information, see:

- FEAT\_SVE.
- Loads and stores - SME, SME2, SVE2p1.
- Data processing - SVE2.

## FEAT\_SVE\_B16B16, Non-widening BFloat16 to BFloat16 arithmetic for SVE2 and SME2

FEAT\_SVE\_B16B16 introduces the following:

- If FEAT\_SVE2 is implemented, the SVE non-widening BFloat16 instructions when the PE is not in Streaming SVE mode.
- If FEAT\_SME2 is implemented, the SVE non-widening BFloat16 instructions when the PE is in Streaming SVE mode, and the SME Z-targeting multi-vector non-widening BFloat16 instructions.

This feature is supported in AArch64 state only.

FEAT\_SVE\_B16B16 is OPTIONAL from Armv9.2.

If FEAT\_SVE\_B16B16 is implemented, then FEAT\_SME2 or FEAT\_SVE2 is implemented.

The following field identifies the presence of FEAT\_SVE\_B16B16:

- ID\_AA64ZFR0\_EL1.B16B16.

For more information, see:

- BFloat16 arithmetic.
- BFloat16 minimum/maximum.
- Clamp to minimum/maximum.

## FEAT\_SYSINSTR128, 128-bit System instructions

FEAT\_SYSINSTR128 introduces support for IMPLEMENTATION DEFINED System instructions that can take 128-bit inputs.

This feature is supported in AArch64 state only.

FEAT\_SYSINSTR128 is OPTIONAL from Armv9.3.

If FEAT\_SYSINSTR128 is implemented, then FEAT\_SCTLR2 is implemented.

If FEAT\_SYSINSTR128 is implemented, then FEAT\_D128 is implemented.

The following field identifies the presence of FEAT\_SYSINSTR128:

- ID\_AA64ISAR2\_EL1.SYSINSTR\_128.

For more information, see The A64 System Instruction Class.

## FEAT\_SYSREG128, 128-bit System registers

FEAT\_SYSREG128 introduces the following support for 128-bit System registers:

- The MRRS instruction to move a 128-bit System register into a pair of 64-bit general-purpose registers.
- The MSRR instruction to move a pair of 64-bit general-purpose registers to a 128-bit System register.
- 128-bit formats of the following system registers:
- The Physical Address Register, PAR\_EL1.
- The Read-Check-Write mask registers, RCWMASK\_EL1 and RCWSMASK\_EL1.
- The following translation table base address registers, TTBR0\_EL1, TTBR0\_EL2, TTBR1\_EL1, TTBR1\_EL2, VTTBR\_EL2.

This feature is supported in AArch64 state only.

FEAT\_SYSREG128 is OPTIONAL from Armv9.3.

If FEAT\_SYSREG128 is implemented, then FEAT\_SCTLR2 is implemented.

If FEAT\_SYSREG128 is implemented, then FEAT\_D128 is implemented.

The following field identifies the presence of FEAT\_SYSREG128:

- ID\_AA64ISAR2\_EL1.SYSREG\_128.

## FEAT\_TRBE\_EXT, Trace Buffer external mode

FEAT\_TRBE\_EXT allows an external debugger, as well as a self-hosted debugger, to use the Trace Buffer Unit. All of the following registers are introduced to determine the parameters of the implementation:

- TRBDEVARCH.
- TRBDEVID.
- TRBDEVID1.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_TRBE\_EXT is OPTIONAL from Armv9.3.

If FEAT\_TRBE\_EXT is implemented, then FEAT\_TRBE is implemented.

The following fields identify the presence of FEAT\_TRBE\_EXT:

- ID\_AA64DFR0\_EL1.ExtTrcBuff.
- EDDFR.TraceBuffer.
- EDDFR.ExtTrcBuff.

For more information, see Trace buffer External mode.

## FEAT\_TRBE\_MPAM, Trace Buffer MPAM extensions

FEAT\_TRBE\_MPAM allows software to program the MPAM PARTID and PMG to use different MPAM values for trace data. TRBDEVID1.{PMG\_MAX, PARTID\_MAX} are used to determine the parameters of the MPAM implementation.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_TRBE\_MPAM is OPTIONAL from Armv9.3.

If FEAT\_TRBE\_MPAM is implemented, then FEAT\_TRBE\_EXT is implemented.

If FEAT\_TRBE\_MPAM is implemented, then FEAT\_MPAM is implemented.

When FEAT\_TRBE\_MPAM and FEAT\_AA64EL2 are implemented, FEAT\_FGT2 is implemented.

The following fields identify the presence of FEAT\_TRBE\_MPAM:

- TRBIDR\_EL1.MPAM.
- TRBIDR\_EL1.MPAM.

For more information, see External mode and FEAT\_MPAM.

## A2.3.5.1 Features added to the Armv9.4 extension in later releases

- FEAT\_RME\_GDI.
- FEAT\_SME\_MOP4.
- FEAT\_SME\_TMOP.
- FEAT\_SSVE\_BitPerm.
- FEAT\_SSVE\_FEXPA.

## A2.3.6 The Armv9.5 architecture extension

The Armv9.5 architecture extension is an extension to Armv9.4. It adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv9.5 compliant if all of the following apply:

- It is Armv9.4 compliant.
- It includes all of the Armv9.5 architectural features that are mandatory.

An Armv9.5 compliant implementation can additionally include:

- Armv9.5 features that are optional.

## FEAT\_ASID2, Support for concurrent use of two ASIDs

FEAT\_ASID2 introduces support for use of one ASID for each TTBR\_ELx.

This feature is supported in AArch64 state only.

FEAT\_ASID2 is OPTIONAL from Armv9.4.

FEAT\_ASID2 is mandatory from Armv9.5.

If FEAT\_ASID2 is implemented, then FEAT\_TCR2 is implemented.

The following field identifies the presence of FEAT\_ASID2:

- ID\_AA64MMFR4\_EL1.ASID2.

For more information, see Use of ASIDs and VMIDs to reduce TLB maintenance requirements.

## FEAT\_BWE2, Breakpoint and watchpoint enhancements 2

FEAT\_BWE2 provides the capability to generate a Watchpoint exception or debug event when software accesses an address outside of one or more user-supplied address regions.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_BWE2 is OPTIONAL from Armv9.4.

In an Armv9.5 implementation, if FEAT\_BWE is implemented, FEAT\_BWE2 is implemented.

If FEAT\_BWE2 is implemented, then FEAT\_BWE is implemented.

The following fields identify the presence of FEAT\_BWE2:

- ID\_AA64DFR2\_EL1.BWE.
- EDDFR2.BWE.

For more information, see:

- About Watchpoint exceptions.
- Exception syndrome information, fault address information, and preferred return address.
- Watchpoint data address comparisons.

## FEAT\_CPA, Instruction-only Checked Pointer Arithmetic

FEAT\_CPA introduces support for Checked Pointer Arithmetic instructions.

This feature is supported in AArch64 state only.

FEAT\_CPA is OPTIONAL from Armv9.4.

FEAT\_CPA is mandatory from Armv9.5.

The following field identifies the presence of FEAT\_CPA:

- ID\_AA64ISAR3\_EL1.CPA.

For more information, see Checked Pointer Arithmetic.

## FEAT\_CPA2, Checked Pointer Arithmetic

FEAT\_CPA2 introduces support for enabling Checked Pointer Arithmetic. Checked Pointer Arithmetic detects and reports corruption of the following:

- The top 8 bits of a pointer.
- Multiplication overflows that lead to invalid array indices being computed.

This feature is supported in AArch64 state only.

FEAT\_CPA2 is OPTIONAL from Armv9.4.

If FEAT\_CPA2 is implemented, then FEAT\_CPA is implemented.

If FEAT\_CPA2 is implemented, then FEAT\_SCTLR2 is implemented.

The following field identifies the presence of FEAT\_CPA2:

- ID\_AA64ISAR3\_EL1.CPA.

For more information, see Checked Pointer Arithmetic.

## FEAT\_E3DSE, Delegated SError exception injection

FEAT\_E3DSE provides an SError injection mechanism for EL3 called delegated SErrors.

This feature is supported in AArch64 state only.

FEAT\_E3DSE is OPTIONAL from Armv9.4.

In an Armv9.5 implementation, if FEAT\_AA64EL3 is implemented, FEAT\_E3DSE is implemented.

The following field identifies the presence of FEAT\_E3DSE:

- ID\_AA64MMFR4\_EL1.E3DSE.

For more information, see Asynchronous exception types.

## FEAT\_ETS3, Enhanced Translation Synchronization

FEAT\_ETS3 introduces support for enhanced memory access ordering requirements for translation table walks.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_ETS3 is OPTIONAL from Armv8.0.

FEAT\_ETS3 is mandatory from Armv9.5.

If FEAT\_ETS3 is implemented, then FEAT\_ETS2 is implemented.

The following fields identify the presence of FEAT\_ETS3:

- ID\_AA64MMFR1\_EL1.ETS.
- ID\_MMFR5\_EL1.ETS.
- ID\_MMFR5.ETS.

For more information, see:

- Ordering requirements defined by the formal concurrency model.
- Ordering of memory accesses from translation table walks.
- Ordering of translation table walks.

## FEAT\_FAMINMAX, Floating-point maximum and minimum absolute value instructions

FEAT\_FAMINMAX introduces the Advanced SIMD, SVE and SME FAMAX and FAMIN instructions that compute floating-point maximum and minimum absolute value.

FEAT\_FAMINMAX is OPTIONAL from Armv9.2.

In an Armv9.5 implementation, if FEAT\_FP is implemented, FEAT\_FAMINMAX is implemented.

If FEAT\_FAMINMAX is implemented, then FEAT\_AdvSIMD, FEAT\_SVE2, or FEAT\_SME2 is implemented.

The following field identifies the presence of FEAT\_FAMINMAX:

- ID\_AA64ISAR3\_EL1.FAMINMAX.

For more information, see:

- SIMD arithmetic.
- Floating-point minimum/maximum absolute value.
- Multi-vector minimum/maximum.

## FEAT\_FGWTE3, Fine-Grained Write Trap EL3

FEAT\_FGWTE3 introduces traps for write accesses at EL3 to individual *\_EL3 System registers. The traps are independent of existing controls. The bits in the control register FGWTE3\_EL3 are sticky, and writes of 0 are ignored.

This feature is supported in AArch64 state only.

FEAT\_FGWTE3 is OPTIONAL from Armv9.4.

If FEAT\_FGWTE3 is implemented, then FEAT\_EL3 is implemented.

The following field identifies the presence of FEAT\_FGWTE3:

- ID\_AA64MMFR4\_EL1.FGWTE3.

For more information, see EL3 configurable instruction controls.

## FEAT\_FP8, FP8 convert instructions

FEAT\_FP8 introduces the following:

- OFP8 formats E5M2 and E4M3 for FP8 instructions.
- Advanced SIMD: FP8 convert instructions and a floating point scaling FSCALE instruction.
- SME: FP8 convert instructions and floating point scaling FSCALE instructions.
- SVE: FP8 convert instructions.

FEAT\_FP8 is OPTIONAL from Armv9.2.

If FEAT\_FP8 is implemented, then FEAT\_FPMR is implemented.

If FEAT\_FP8 is implemented, then FEAT\_FAMINMAX is implemented.

If FEAT\_FP8 is implemented, then FEAT\_LUT is implemented.

If FEAT\_FP8 is implemented, then FEAT\_BF16 is implemented.

If FEAT\_FP8 is implemented, then FEAT\_AdvSIMD, FEAT\_SVE2, or FEAT\_SME2 is implemented.

The following fields identify the presence of FEAT\_FP8:

- ID\_AA64FPFR0\_EL1.F8CVT.
- ID\_AA64FPFR0\_EL1.F8E4M3.
- ID\_AA64FPFR0\_EL1.F8E5M2.

For more information, see:

- FP8 floating-point formats.
- Summary of FP8 instruction behaviors.
- For Advanced SIMD, FP8 floating-point conversion.
- For SVE, FP8 floating-point conversions.
- For SME, FP8 floating-point conversions.
- The OCP8-bit Floating Point Specification (OFP8) .

## FEAT\_FP8DOT2, FP8 2-way dot product to half-precision instructions

FEAT\_FP8DOT2 introduces the Advanced SIMD FP8 to half-precision 2-way dot product instructions.

If FEAT\_SVE2 is implemented, FEAT\_FP8DOT2 also implements the SVE versions of these instructions.

Note

This feature does not enable execution of the SVE instructions in Streaming SVE mode.

FEAT\_FP8DOT2 is OPTIONAL from Armv9.2.

If FEAT\_FP8DOT2 is implemented, then FEAT\_FP8DOT4 is implemented.

If FEAT\_FP8DOT2 is implemented, then FEAT\_AdvSIMD or FEAT\_SVE2 is implemented.

The following field identifies the presence of FEAT\_FP8DOT2:

- ID\_AA64FPFR0\_EL1.F8DP2.

For more information, see:

- Summary of FP8 instruction behaviors.
- For Advanced SIMD, FP8 floating-point dot product.
- For SVE, FP8 floating-point dot product.

## FEAT\_FP8DOT4, FP8 4-way dot product to single-precision instructions

FEAT\_FP8DOT4 introduces the following:

- Advanced SIMD: FP8 to single-precision 4-way dot product instructions.
- SVE: SVE FP8 to single-precision 4-way dot product instructions.

Note

This feature does not enable execution of the SVE instructions in Streaming SVE mode.

FEAT\_FP8DOT4 is OPTIONAL from Armv9.2.

If FEAT\_FP8DOT4 is implemented, then FEAT\_FP8FMA is implemented.

If FEAT\_FP8DOT4 is implemented, then FEAT\_AdvSIMD or FEAT\_SVE2 is implemented.

The following field identifies the presence of FEAT\_FP8DOT4:

- ID\_AA64FPFR0\_EL1.F8DP4.

For more information, see:

- Summary of FP8 instruction behaviors.
- For Advanced SIMD, FP8 floating-point dot product.
- For SVE, FP8 floating-point dot product.

## FEAT\_FP8FMA, FP8 multiply-accumulate to half-precision and single-precision instructions

FEAT\_FP8FMA introduces the following:

- Advanced SIMD: FP8 to half-precision and single-precision multiply-accumulate instructions.
- SVE: FP8 to half-precision and single-precision multiply-accumulate instructions.

Note

This feature does not enable execution of the SVE instructions in Streaming SVE mode.

FEAT\_FP8FMA is OPTIONAL from Armv9.2.

If FEAT\_FP8FMA is implemented, then FEAT\_FP8 is implemented.

If FEAT\_FP8FMA is implemented, then FEAT\_AdvSIMD or FEAT\_SVE2 is implemented.

The following field identifies the presence of FEAT\_FP8FMA:

- ID\_AA64FPFR0\_EL1.F8FMA.

For more information, see:

- Summary of FP8 instruction behaviors.
- For Advanced SIMD, FP8 floating-point widening multiply-accumulate.
- For SVE, FP8 floating-point widening multiply-accumulate.

## FEAT\_FPMR, Floating-point Mode Register

FEAT\_FPMR introduces the Special-purpose register FPMR.

FEAT\_FPMR is OPTIONAL from Armv9.2.

If FEAT\_FPMR is implemented, then FEAT\_AdvSIMD is implemented.

When FEAT\_FPMR and FEAT\_EL2 are implemented, FEAT\_FGT is implemented.

When FEAT\_FPMR and FEAT\_EL2 are implemented, FEAT\_HCX is implemented.

The following field identifies the presence of FEAT\_FPMR:

- ID\_AA64PFR2\_EL1.FPMR.

For more information, see Summary of FP8 instruction behaviors.

## FEAT\_HACDBS, Hardware accelerator for cleaning Dirty state

FEAT\_HACDBS introduces the Hardware accelerator for cleaning Dirty state, which enhances the process of updating stage 2 descriptors from writable-dirty to writable-clean.

This feature is supported in AArch64 state only.

FEAT\_HACDBS is OPTIONAL from Armv9.4.

If FEAT\_HACDBS is implemented, then FEAT\_HDBSS is implemented.

The following field identifies the presence of FEAT\_HACDBS:

- ID\_AA64MMFR4\_EL1.HACDBS.

For more information, see Hardware accelerator for cleaning dirty state.

## FEAT\_HDBSS, Hardware Dirty state tracking structure

FEAT\_HDBSS introduces the Hardware Dirty state tracking structure, which enhances tracking the dirty state of stage 2 translation table descriptors.

This feature is supported in AArch64 state only.

FEAT\_HDBSS is OPTIONAL from Armv9.4.

If FEAT\_HDBSS is implemented, then FEAT\_HAFDBS is implemented.

If FEAT\_HDBSS is implemented, then FEAT\_AA64EL2 is implemented.

The following field identifies the presence of FEAT\_HDBSS:

- ID\_AA64MMFR1\_EL1.HAFDBS.

For more information, see Hardware dirty state tracking structure.

## FEAT\_LUT, Lookup table instructions with 2-bit and 4-bit indices

FEAT\_LUT introduces the following lookup table instructions with 2-bit and 4-bit indices:

- The Advanced SIMD LUTI2 and LUTI4 instructions.
- If FEAT\_SVE2 is implemented, the SVE LUTI2 and LUTI4 instructions when the PE is not in Streaming SVE mode.
- If FEAT\_SME2 is implemented, the SVE LUTI2 and LUTI4 instructions when the PE is in Streaming SVE mode.

FEAT\_LUT is OPTIONAL from Armv9.2.

In an Armv9.5 implementation, if FEAT\_AdvSIMD is implemented, FEAT\_LUT is implemented.

If FEAT\_LUT is implemented, then FEAT\_AdvSIMD, FEAT\_SVE2, or FEAT\_SME2 is implemented.

The following field identifies the presence of FEAT\_LUT:

- ID\_AA64ISAR2\_EL1.LUT.

For more information, see:

- For Advanced SIMD, Lookup table using 2-bit or 4-bit indices.
- For SVE, Lookup table using 2-bit or 4-bit indices.

## FEAT\_PAuth\_LR, Pointer authentication instructions that allow signing of LR using SP and PC as diversifiers

FEAT\_PAuth\_LR introduces instructions that allow signing of the 64-bit value in LR against the value of SP, and a PC-relative instruction address.

This feature is supported in AArch64 state only.

FEAT\_PAuth\_LR is OPTIONAL from Armv9.4.

If FEAT\_PAuth\_LR is implemented, then FEAT\_FPACCOMBINE is implemented.

If FEAT\_PAuth\_LR is implemented, then FEAT\_SCTLR2 is implemented.

When FEAT\_PAuth\_LR and FEAT\_AA64EL2 are implemented, FEAT\_HCX is implemented.

The following fields identify the presence of FEAT\_PAuth\_LR:

- ID\_AA64ISAR1\_EL1.APA.
- ID\_AA64ISAR1\_EL1.API.
- ID\_AA64ISAR2\_EL1.APA3.

## FEAT\_PMUv3\_SME, Performance Monitors extensions for SME

FEAT\_PMUv3\_SME supports filtering to control counting events in Streaming and Non-streaming SVE modes.

This feature is supported in AArch64 state only.

FEAT\_PMUv3\_SME is OPTIONAL from Armv9.4.

In an Armv9.5 implementation, if FEAT\_PMUv3 and FEAT\_SME are implemented, FEAT\_PMUv3\_SME is implemented.

If FEAT\_PMUv3\_SME is implemented, then FEAT\_PMUv3 is implemented.

If FEAT\_PMUv3\_SME is implemented, then FEAT\_SME is implemented.

The following field identifies the presence of FEAT\_PMUv3\_SME:

- PMMIR\_EL1.SME.

For more information, see Filtering by SVE Streaming mode.

## FEAT\_PMUv3\_TH2, Performance Monitors event counter linking extension

FEAT\_PMUv3\_TH2 extends the Performance Monitors Extension to add the ability to program an event counter to count the logical combination of two events.

This feature is supported in both AArch64 and AArch32 states. The threshold condition controls are accessible only in AArch64 state. However, threshold conditions still apply in AArch32 state.

FEAT\_PMUv3\_TH2 is OPTIONAL from Armv9.4.

If FEAT\_PMUv3\_TH2 is implemented, then FEAT\_PMUv3\_TH is implemented.

If FEAT\_PMUv3\_TH2 is implemented, then FEAT\_PMUv3\_EDGE is implemented.

The following fields identify the presence of FEAT\_PMUv3\_TH2:

- PMMIR\_EL1.EDGE.
- PMMIR.EDGE.

For more information, see Event threshold and edge counting.

## FEAT\_RME\_GPC2, RME Granule Protection Check 2 Extension

FEAT\_RME\_GPC2 introduces two mechanisms to the GPC that enable memory isolation models:

- Non-secure Only GPI encoding.
- Physical Address Space Disable.

This feature is supported in AArch64 state only.

FEAT\_RME\_GPC2 is OPTIONAL from Armv9.4.

If FEAT\_RME\_GPC2 is implemented, then FEAT\_RME is implemented.

The following field identifies the presence of FEAT\_RME\_GPC2:

- ID\_AA64PFR0\_EL1.RME.

For more information, see:

- GPC faults.
- GPI field encoding in GPT descriptors.

## FEAT\_SME\_F8F16, SME2ZA-targeting FP8 multiply-accumulate, dot product, and outer product to half-precision instructions

FEAT\_SME\_F8F16 introduces the following SME instructions:

- ZA-targeting FP8 to half-precision multiply-accumulate, dot product, and outer product instructions.
- ZA-targeting multi-vector non-widening half-precision FADD and FSUB instructions.

FEAT\_SME\_F8F16 is OPTIONAL from Armv9.2.

If FEAT\_SME\_F8F16 is implemented, then FEAT\_SME\_F8F32 is implemented.

The following field identifies the presence of FEAT\_SME\_F8F16:

- ID\_AA64SMFR0\_EL1.F8F16.

For more information, see:

- Summary of FP8 instruction behaviors.
- FP8 floating-point widening multiply-accumulate.
- FP8 floating-point dot product.
- FP8 floating-point outer product.

## FEAT\_SME\_F8F32, SME2 ZA-targeting FP8 multiply-accumulate, dot product, and outer product to singleprecision instructions

FEAT\_SME\_F8F32 introduces the SME ZA-targeting FP8 to single-precision multiply-accumulate, dot product, and outer product instructions.

FEAT\_SME\_F8F32 is OPTIONAL from Armv9.2.

If FEAT\_SME\_F8F32 is implemented, then FEAT\_SME2 is implemented.

If FEAT\_SME\_F8F32 is implemented, then FEAT\_FP8 is implemented.

The following field identifies the presence of FEAT\_SME\_F8F32:

- ID\_AA64SMFR0\_EL1.F8F32.

For more information, see:

- Summary of FP8 instruction behaviors.
- FP8 floating-point widening multiply-accumulate.
- FP8 floating-point dot product.
- FP8 floating-point outer product.

## FEAT\_SME\_LUTv2, Lookup table instructions with 4-bit indices and 8-bit elements

FEAT\_SME\_LUTv2 introduces the following:

- The LUTI4 (four registers, 8-bit) instruction.
- The MOVT (vector to table) instruction.

FEAT\_SME\_LUTv2 is OPTIONAL from Armv9.2.

If FEAT\_SME\_LUTv2 is implemented, then FEAT\_SME2 is implemented.

The following field identifies the presence of FEAT\_SME\_LUTv2:

- ID\_AA64SMFR0\_EL1.LUTv2.

## FEAT\_SPE\_ALTCLK, Statistical Profiling alternate clock domain extension

FEAT\_SPE\_ALTCLK supports collection of timing data using the Statistical Profiling Extension when profiling a PE that includes asynchronous accelerators, such as a Streaming Mode Compute Unit (SMCU).

This feature is supported in AArch64 state only.

FEAT\_SPE\_ALTCLK is OPTIONAL from Armv9.4.

If FEAT\_SPE\_ALTCLK is implemented, then FEAT\_SPE is implemented.

The following field identifies the presence of FEAT\_SPE\_ALTCLK:

- PMSIDR\_EL1.ALTCLK.

For more information, see Asynchronous operation.

## FEAT\_SPE\_EFT, Statistical Profiling extended filtering by type

FEAT\_SPE\_EFT extends SPE filtering to support targeted profiling of floating-point and SIMD operations.

This feature is supported in AArch64 state only.

FEAT\_SPE\_EFT is OPTIONAL from Armv9.4.

In an Armv9.5 implementation, if FEAT\_SPE is implemented, FEAT\_SPE\_EFT is implemented.

If FEAT\_SPE\_EFT is implemented, then FEAT\_SPE is implemented.

If FEAT\_SPE\_EFT is implemented, then FEAT\_SPE\_FPF is implemented.

The following field identifies the presence of FEAT\_SPE\_EFT:

- PMSIDR\_EL1.EFT.

For more information, see Filtering by operation type.

## FEAT\_SPE\_FPF, Statistical Profiling floating-point and SIMD flag extension

FEAT\_SPE\_FPF extends the profiling information recorded by the Statistical Profiling Extension to identify sampled scalar floating-point and Advanced SIMD instructions.

This feature is supported in AArch64 state only.

FEAT\_SPE\_FPF is OPTIONAL from Armv9.4.

In an Armv9.5 implementation, if FEAT\_SPE is implemented, FEAT\_SPE\_FPF is implemented.

If FEAT\_SPE\_FPF is implemented, then FEAT\_SPE is implemented.

If FEAT\_SPE\_FPF is implemented, then FEAT\_SPE\_EFT is implemented.

The following field identifies the presence of FEAT\_SPE\_FPF:

- PMSIDR\_EL1.FPF.

For more information, see Additional information for other operations.

## FEAT\_SPE\_SME, Statistical Profiling extensions for SME

FEAT\_SPE\_SME provides support for profiling of software that uses SME instructions using the Statistical Profiling Extension.

This feature is supported in AArch64 state only.

FEAT\_SPE\_SME is OPTIONAL from Armv9.2.

In an Armv9.5 implementation, if FEAT\_SPEv1p1 and FEAT\_SME are implemented, FEAT\_SPE\_SME is implemented.

If FEAT\_SPE\_SME is implemented, then FEAT\_SPEv1p1 is implemented.

If FEAT\_SPE\_SME is implemented, then FEAT\_SME is implemented.

The following field identifies the presence of FEAT\_SPE\_SME:

- PMSIDR\_EL1.SME.

For more information, see Additional information for each profiled SVE and SME operation.

## FEAT\_SPMU2, System Performance Monitors Extension version 2

FEAT\_SPMU2 provides the functionality to set multiple event counters in a System PMU to zero in a single operation.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_SPMU2 is OPTIONAL from Armv9.4.

If FEAT\_SPMU and v9Ap5 are implemented, then FEAT\_SPMU2 is implemented.

If FEAT\_SPMU2 is implemented, then FEAT\_SPMU is implemented.

The following field identifies the presence of FEAT\_SPMU2:

- ID\_AA64DFR1\_EL1.SPMU.

For more information, see Zeroing System PMU counters.

## FEAT\_SSVE\_FP8DOT2, SVE FP8 2-way dot product to half-precision instructions in Streaming SVE mode

FEAT\_SSVE\_FP8DOT2 enables execution of SVE FP8 to half-precision 2-way dot product instructions in Streaming SVE mode.

FEAT\_SSVE\_FP8DOT2 is OPTIONAL from Armv9.2.

If FEAT\_SSVE\_FP8DOT2 is implemented, then FEAT\_SSVE\_FP8DOT4 is implemented.

If FEAT\_SME2 and FEAT\_FP8DOT2 are implemented, then FEAT\_SSVE\_FP8DOT2 is implemented.

The following field identifies the presence of FEAT\_SSVE\_FP8DOT2:

- ID\_AA64SMFR0\_EL1.SF8DP2.

For more information, see:

- Summary of FP8 instruction behaviors.
- FP8 floating-point dot product.

## FEAT\_SSVE\_FP8DOT4, SVE2 FP8 4-way dot product to single-precision instructions in Streaming SVE mode

FEAT\_SSVE\_FP8DOT4 enables execution of SVE FP8 to single-precision 4-way dot product instructions in Streaming SVE mode.

FEAT\_SSVE\_FP8DOT4 is OPTIONAL from Armv9.2.

If FEAT\_SSVE\_FP8DOT4 is implemented, then FEAT\_SSVE\_FP8FMA is implemented.

If FEAT\_SME2 and FEAT\_FP8DOT4 are implemented, then FEAT\_SSVE\_FP8DOT4 is implemented.

The following field identifies the presence of FEAT\_SSVE\_FP8DOT4:

- ID\_AA64SMFR0\_EL1.SF8DP4.

For more information, see:

- Summary of FP8 instruction behaviors.
- FP8 floating-point dot product.

## FEAT\_SSVE\_FP8FMA, SVE2 FP8 multiply-accumulate to half-precision and single-precision instructions in Streaming SVE mode

FEAT\_SSVE\_FP8FMA enables execution of SVE FP8 to half-precision and single-precision multiply-accumulate instructions in Streaming SVE mode.

FEAT\_SSVE\_FP8FMA is OPTIONAL from Armv9.2.

If FEAT\_SSVE\_FP8FMA is implemented, then FEAT\_FP8 is implemented.

If FEAT\_SSVE\_FP8FMA is implemented, then FEAT\_SME2 is implemented.

If FEAT\_SME2 and FEAT\_FP8FMA are implemented, then FEAT\_SSVE\_FP8FMA is implemented.

The following field identifies the presence of FEAT\_SSVE\_FP8FMA:

- ID\_AA64SMFR0\_EL1.SF8FMA.

For more information, see:

- Summary of FP8 instruction behaviors.
- FP8 floating-point widening multiply-accumulate.

## FEAT\_STEP2, Enhanced Software Step Extension

FEAT\_STEP2 introduces support for a debugger to control the instruction executed by the PE when single-stepping, without modifying the instruction in memory.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_STEP2 is OPTIONAL from Armv9.4.

FEAT\_STEP2 is mandatory from Armv9.5.

When FEAT\_STEP2 and FEAT\_EL2 are implemented, FEAT\_FGT2 is implemented.

The following field identifies the presence of FEAT\_STEP2:

- ID\_AA64DFR2\_EL1.STEP.

For more information, see Behavior in the active-not-pending state.

## FEAT\_TLBIW, TLBI VMALL for Dirty state

FEAT\_TLBIW provides the following TLBI instructions that remove the stage 2 dirty state from TLB entries:

- TLBI VMALLWS2E1, TLBI VMALLWS2E1NXS.
- TLBI VMALLWS2E1IS, TLBI VMALLWS2E1ISNXS.
- TLBI VMALLWS2E1OS, TLBI VMALLWS2E1OSNXS.

This feature is supported in AArch64 state only.

FEAT\_TLBIW is OPTIONAL from Armv9.4.

If FEAT\_TLBIW is implemented, then FEAT\_AA64EL2 is implemented.

The following field identifies the presence of FEAT\_TLBIW:

- ID\_AA64ISAR3\_EL1.TLBIW.

## A2.3.7 The Armv9.6 architecture extension

The Armv9.6 architecture extension is an extension to Armv9.5. It adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv9.6 compliant if all of the following apply:

- It is Armv9.5 compliant.
- It includes all of the Armv9.6 architectural features that are mandatory.

An Armv9.6 compliant implementation can additionally include:

- Armv9.6 features that are optional.

## FEAT\_AMU\_EXTACR, Activity Monitors External Control Register

FEAT\_AMU\_EXTACR implements a control register to enable access to the Activity Monitors External registers.

- If FEAT\_RME is implemented, the register AMROOTCR is implemented to control Root, Realm, Secure and Non-secure accesses to the external AMU registers.
- If FEAT\_RME is not implemented, the register AMSCR is implemented to control Secure and Non-secure accesses to the external AMU registers.

FEAT\_AMU\_EXTACR is OPTIONAL from Armv8.4.

If FEAT\_AMU\_EXTACR is implemented, then FEAT\_AMU\_EXT is implemented.

For more information, see The Activity Monitors Extension.

## FEAT\_CMPBR, Compare and Branch instructions

FEAT\_CMPBR introduces the A64 base compare and branch instructions.

This feature is supported in AArch64 state only.

FEAT\_CMPBR is OPTIONAL from Armv9.5.

FEAT\_CMPBR is mandatory from Armv9.6.

The following field identifies the presence of FEAT\_CMPBR:

- ID\_AA64ISAR2\_EL1.CSSC.

For more information, see:

- 'Conditional branch'.
- 'Concurrent modification and execution of instructions'.

## FEAT\_F8F16MM, 8-bit floating-point matrix multiply-accumulate to half-precision

FEAT\_F8F16MM introduces the Advanced SIMD 8-bit floating-point matrix multiply-accumulate to half-precision instruction.

If FEAT\_SVE2 is implemented, FEAT\_F8F16MM implements the SVE 8-bit floating-point matrix multiply-accumulate to half-precision instruction, when the PE is not in Streaming SVE mode.

This feature is supported in AArch64 state only.

FEAT\_F8F16MM is OPTIONAL from Armv9.2.

If FEAT\_F8F16MM is implemented, then FEAT\_F8F32MM is implemented.

If FEAT\_F8F16MM is implemented, then FEAT\_FP8DOT2 is implemented.

The following field identifies the presence of FEAT\_F8F16MM:

- ID\_AA64FPFR0\_EL1.F8MM4.

For more information, see:

- For Advanced SIMD: 'FP8 matrix multiply-accumulate'.
- For SVE: 'FP8 floating-point matrix multiply-accumulate'.

## FEAT\_F8F32MM, 8-bit floating-point matrix multiply-accumulate to single-precision

FEAT\_F8F32MM introduces the Advanced SIMD 8-bit floating-point matrix multiply-accumulate to single-precision instruction.

If FEAT\_SVE2 is implemented, FEAT\_F8F32MM implements the SVE 8-bit floating-point matrix multiply-accumulate to single-precision instruction, when the PE is not in Streaming SVE mode.

This feature is supported in AArch64 state only.

FEAT\_F8F32MM is OPTIONAL from Armv9.2.

If FEAT\_F8F32MM is implemented, then FEAT\_FP8DOT4 is implemented.

The following field identifies the presence of FEAT\_F8F32MM:

- ID\_AA64FPFR0\_EL1.F8MM8.

For more information, see:

- For Advanced SIMD: 'FP8 matrix multiply-accumulate'.
- For SVE: 'FP8 floating-point matrix multiply-accumulate'.

## FEAT\_FPRCVT, Floating-Point to/from Integer in Scalar FP register

FEAT\_FPRCVT introduces A64 base floating-point to integer and integer to floating-point convert instructions with only scalar SIMD&amp;FP register operands and results, and with different input and output register sizes.

FEAT\_FPRCVT implements the Advanced SIMD scalar floating-point to integer and integer to floating-point convert instructions with only scalar SIMD&amp;FP register operands and results, and with different and same input and output register sizes, when the PE is in Streaming SVE mode.

This feature is supported in AArch64 state only.

FEAT\_FPRCVT is OPTIONAL from Armv9.5.

If FEAT\_FP and v9Ap6 are implemented, then FEAT\_FPRCVT is implemented.

If FEAT\_FPRCVT is implemented, then FEAT\_FP is implemented.

The following field identifies the presence of FEAT\_FPRCVT:

- ID\_AA64ISAR3\_EL1.FPRCVT.

For more information, see:

- 'Floating-point conversion'.

## FEAT\_IDTE3, Trapping ID register accesses to EL3

FEAT\_IDTE3 introduces support for trapping ID register accesses to EL3.

This feature is supported in AArch64 state only.

In an Armv9.6 implementation, if FEAT\_EL3 is implemented, FEAT\_IDTE3 is implemented.

FEAT\_IDTE3 is OPTIONAL from Armv9.0.

The following field identifies the presence of FEAT\_IDTE3:

- ID\_AA64MMFR2\_EL1.IDS.

## FEAT\_LS64WB, LS64 for Write-back cacheable memory

FEAT\_LS64WB provides support for large single-copy atomic load and store instructions for accesses to Conventional memory to enable scalability of atomic message passing without relying on separate flag and data accesses.

This feature is supported in AArch64 state only.

FEAT\_LS64WB is OPTIONAL from Armv9.2.

If FEAT\_LS64WB is implemented, then FEAT\_LS64\_ACCDATA is implemented.

The following field identifies the presence of FEAT\_LS64WB:

- ID\_AA64ISAR1\_EL1.LS64.

## FEAT\_LSFE, Large System Float Extension

FEAT\_LSFE implements A64 base Atomic floating-point in-memory instructions.

This feature is supported in AArch64 state only.

FEAT\_LSFE is OPTIONAL from Armv9.3.

If FEAT\_LSFE is implemented, then FEAT\_FP is implemented.

The following field identifies the presence of FEAT\_LSFE:

- ID\_AA64ISAR3\_EL1.LSFE.

For more information, see:

- 'Atomic floating-point memory operations'.

## FEAT\_LSUI, Unprivileged Load Store

FEAT\_LSUI introduces unprivileged variants of load and store instructions so that clearing PSTATE.PAN is never required in privileged software.

This feature is supported in AArch64 state only.

FEAT\_LSUI is OPTIONAL from Armv9.5.

FEAT\_LSUI is mandatory from Armv9.6.

The following field identifies the presence of FEAT\_LSUI:

- ID\_AA64ISAR3\_EL1.LSUI.

## FEAT\_MPAM\_MSC\_DCTRL, MPAM Default Resource Control

FEAT\_MPAM\_MSC\_DCTRL introduces support in an MSC for a default resource control configuration, which is applied to requests with PARTIDs outside the MSC's supported range, or with PARTIDs for which there is no configuration set.

This feature is supported in AArch64 state only.

FEAT\_MPAM\_MSC\_DCTRL is OPTIONAL from Armv9.5.

If FEAT\_MPAM\_MSC\_DCTRL is implemented, then FEAT\_MPAMv1p1 or FEAT\_MPAMv0p1 is implemented.

The following field identifies the presence of FEAT\_MPAM\_MSC\_DCTRL:

- MPAMF\_IDR.HAS\_DEFAULT\_PARTID.

## FEAT\_MPAM\_MSC\_DOMAINS, MPAM Domains Identifier Translation

FEAT\_MPAM\_MSC\_DOMAINS introduces support for MSCs to manipulate the MPAM information bundle by applying PARTID ingress translation, egress translation, or both.

This feature is supported in AArch64 state only.

FEAT\_MPAM\_MSC\_DOMAINS is OPTIONAL from Armv9.5.

If FEAT\_MPAM\_MSC\_DOMAINS is implemented, then FEAT\_MPAMv1p1 or FEAT\_MPAMv0p1 is implemented.

The following fields identify the presence of FEAT\_MPAM\_MSC\_DOMAINS:

- MPAMF\_IDR.HAS\_IN\_TL.
- MPAMF\_IDR.HAS\_OUT\_TL.

## FEAT\_MPAM\_PE\_BW\_CTRL, MPAM PE-side Bandwidth Controls

FEAT\_MPAM\_PE\_BW\_CTRL introduces support for PE-side bandwidth controls.

This feature is supported in AArch64 state only.

FEAT\_MPAM\_PE\_BW\_CTRL is OPTIONAL from Armv9.3.

If FEAT\_MPAM\_PE\_BW\_CTRL is implemented, then FEAT\_MPAMv1p1 or FEAT\_MPAMv0p1 is implemented.

The following field identifies the presence of FEAT\_MPAM\_PE\_BW\_CTRL:

- MPAMIDR\_EL1.HAS\_BW\_CTRL.

## FEAT\_NV2p1, Enhanced nested virtualization support

FEAT NV2p1 further supports nested virtualization by ensuring that control bits in EL1 registers are stateful if the corresponding bits in the corresponding EL2 registers are stateful. This is to prevent loss of the Guest hypervisor's state, and to permit the Host hypervisor to correctly emulate the EL2 environment.

This feature is supported in AArch64 state only.

FEAT\_NV2p1 is OPTIONAL from Armv8.4.

In an Armv9.6 implementation, if FEAT\_NV is implemented, FEAT\_NV2p1 is implemented.

If FEAT\_NV2p1 is implemented, then FEAT\_NV2 is implemented.

The following field identifies the presence of FEAT\_NV2p1:

- ID\_AA64MMFR4\_EL1.NV\_frac.

## FEAT\_OCCMO, Outer Cacheable Cache Maintenance Operation

FEAT\_OCCMO introduces the DC CIVAOC system instruction that provides software with a mechanism to publish writes to the Outer cache level.

This feature is supported in AArch64 state only.

FEAT\_OCCMO is OPTIONAL from Armv9.3.

FEAT\_OCCMO is mandatory from Armv9.6.

The following field identifies the presence of FEAT\_OCCMO:

- ID\_AA64ISAR3\_EL1.OCCMO.

## FEAT\_PCDPHINT, Producer-Consumer Data Placement Hints

FEAT\_PCDPHINT provides hint instructions to indicate each of the following:

- Astore in the current execution thread is generating data at a specific location, which a thread of execution on one or more other observers is waiting on.
- The thread of execution on the current PE will read a location that may not yet have been written with the value to be consumed.

This feature is supported in AArch64 state only.

FEAT\_PCDPHINT is OPTIONAL from Armv9.0.

The following field identifies the presence of FEAT\_PCDPHINT:

- ID\_AA64ISAR2\_EL1.PCDPHINT.

## FEAT\_PMUv3\_EXTPMN, Reserving PMU event counters for external agents

FEAT\_PMUv3\_EXTPMN provides external agents with a mechanism to reserve event counters for external use.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_PMUv3\_EXTPMN is OPTIONAL from Armv9.5.

If FEAT\_PMUv3\_EXTPMN is implemented, then FEAT\_PMUv3\_EXT is implemented.

If FEAT\_PMUv3\_EXTPMN is implemented, then FEAT\_FGT is implemented.

When FEAT\_PMUv3\_EXTPMN and FEAT\_EL2 are implemented, FEAT\_HPMN0 is implemented.

The following field identifies the presence of FEAT\_PMUv3\_EXTPMN:

- PMDEVID.EXTPMN.

## FEAT\_PoPS, Point of Physical Storage

FEAT\_PoPS defines the Point of Physical Storage (PoPS) and introduces System instructions to clean and invalidate to the PoPS.

This feature is supported in AArch64 state only.

FEAT\_PoPS is OPTIONAL from Armv9.5.

The following field identifies the presence of FEAT\_PoPS:

- ID\_AA64MMFR4\_EL1.PoPS.

For more information, see Terminology for Clean, Invalidate, and Clean and Invalidate instructions.

## FEAT\_RME\_GDI, RME Granular Data Isolation extension

FEAT\_RME\_GDI introduces additional GPT GPI encodings to enable memory isolation of non-PE data flows from the PEs, within an RME system.

This feature is supported in AArch64 state only.

FEAT\_RME\_GDI is OPTIONAL from Armv9.4.

If FEAT\_RME\_GDI is implemented, then FEAT\_RME is implemented.

If FEAT\_RME\_GDI is implemented, then FEAT\_RME\_GPC2 is implemented.

The following field identifies the presence of FEAT\_RME\_GDI:

- ID\_AA64MMFR4\_EL1.RMEGDI.

## FEAT\_RME\_GPC3, RME Granule Protection Check 3 Extension

FEAT\_RME\_GPC3 introduces a method for defining a set of windows in the memory map for which Granule Protection Table lookups are skipped, and instead applies a set of default settings associated with the window.

FEAT\_RME\_GPC3 introduces the APAS system instruction, which provides an architected mechanism for directly programming the PA space association for regions of memory that support memory-side dynamic PA space association.

This feature is supported in AArch64 state only.

FEAT\_RME\_GPC3 is OPTIONAL from Armv9.5.

If FEAT\_RME\_GPC3 is implemented, then FEAT\_RME is implemented.

If FEAT\_RME\_GPC3 is implemented, then FEAT\_RME\_GPC2 is implemented.

The following field identifies the presence of FEAT\_RME\_GPC3:

- ID\_AA64PFR0\_EL1.RME.

## FEAT\_SME2p2, Scalable Matrix Extension version 2.2

The Scalable Matrix Extension version 2.2 (SME2.2) is a superset of SME2.1 that adds:

- SMEmulti-vector Z-targeting non-widening floating-point FMUL instruction.
- Quarter-tile outer product instructions.
- Structured sparsity outer product instructions.
- Support for SVE2.2 instructions in Streaming SVE mode.

This feature is supported in AArch64 state only.

FEAT\_SME2p2 is OPTIONAL from Armv9.5.

In an Armv9.6 implementation, if FEAT\_SME is implemented, FEAT\_SME2p2 is implemented.

If FEAT\_SME2p2 is implemented, then FEAT\_SME2p1 is implemented.

If FEAT\_SME2p2 is implemented, then FEAT\_SME\_MOP4 is implemented.

If FEAT\_SME2p2 is implemented, then FEAT\_SME\_TMOP is implemented.

If FEAT\_SME2p2 is implemented, then FEAT\_SSVE\_FEXPA is implemented.

If FEAT\_SME and FEAT\_SVE2p2 are implemented, then FEAT\_SME2p2 is implemented.

The following field identifies the presence of FEAT\_SME2p2:

- ID\_AA64SMFR0\_EL1.SMEver.

For more information, see:

- The Scalable Matrix Extension.
- 'Multi-vector multiply'.
- 'Quarter-tile outer product'.
- 'Structured sparsity outer product'.

## FEAT\_SME\_MOP4, Quarter-tile outer product instructions

FEAT\_SME\_MOP4 introduces the SME Quarter-tile outer product instructions

FEAT\_SME\_MOP4 is OPTIONAL from Armv9.4.

If FEAT\_SME\_MOP4 is implemented, then FEAT\_SME2p1 is implemented.

The following field identifies the presence of FEAT\_SME\_MOP4:

- ID\_AA64SMFR0\_EL1.SMOP4.

For more information, see:

- 'Quarter-tile outer product'.

## FEAT\_SME\_TMOP, Structured sparsity outer product instructions

FEAT\_SME\_TMOP introduces the SME Structured sparsity outer product instructions.

FEAT\_SME\_TMOP is OPTIONAL from Armv9.4.

If FEAT\_SME\_TMOP is implemented, then FEAT\_SME2p1 is implemented.

The following field identifies the presence of FEAT\_SME\_TMOP:

- ID\_AA64SMFR0\_EL1.STMOP.

For more information, see:

- 'Structured sparsity outer product'.

## FEAT\_SPE\_EXC, SPE Profiling exception extension

FEAT\_SPE\_EXC provides support for reporting Profiling Buffer management events as SPE Profiling exceptions.

This feature is supported in AArch64 state only.

FEAT\_SPE\_EXC is OPTIONAL from Armv9.5.

If FEAT\_SPE\_EXC is implemented, then FEAT\_SPEv1p5 is implemented.

The following field identifies the presence of FEAT\_SPE\_EXC:

- ID\_AA64DFR2\_EL1.SPE\_EXC.

## FEAT\_SPE\_nVM, Statistical Profiling physical addressing mode extension

FEAT\_SPE\_nVM provides support for defining the Profiling Buffer using physical addresses or intermediate physical addresses.

This feature is supported in AArch64 state only.

FEAT\_SPE\_nVM is OPTIONAL from Armv9.5.

If FEAT\_SPE\_nVM is implemented, then FEAT\_SPE is implemented.

When FEAT\_SPE\_nVM and FEAT\_EL2 are implemented, FEAT\_FGT2 is implemented.

The following field identifies the presence of FEAT\_SPE\_nVM:

- ID\_AA64DFR2\_EL1.SPE\_nVM.

## FEAT\_SPEv1p5, Statistical Profiling Extension version 1.5

FEAT\_SPEv1p5 introduces the following to the Statistical Profiling Extension:

- If EL2 and FEAT\_FGT are implemented, a fine-grained trap on the PSB CSYNC instruction.
- The SPE Profiling exception extension, FEAT\_SPE\_EXC.
- The Statistical Profiling physical addressing mode extension, FEAT\_SPE\_nVM.

This feature is supported in AArch64 state only.

FEAT\_SPEv1p5 is OPTIONAL from Armv9.5.

In an Armv9.6 implementation, if FEAT\_SPE is implemented, FEAT\_SPEv1p5 is implemented.

If FEAT\_SPEv1p5 is implemented, then FEAT\_SPEv1p4 is implemented.

If FEAT\_SPEv1p5 is implemented, then FEAT\_SPE\_CRR is implemented.

If FEAT\_SPEv1p5 is implemented, then FEAT\_SPE\_EXC is implemented.

If FEAT\_SPEv1p5 is implemented, then FEAT\_SPE\_nVM is implemented.

The following field identifies the presence of FEAT\_SPEv1p5:

- ID\_AA64DFR0\_EL1.PMSVer.

## FEAT\_SRMASK, Bitwise System Register Write Masks

FEAT\_SRMASK introduces aliases and bitwise write masks for EL1 control registers to reduce trapping of EL1 System register accesses to EL2. The equivalent bitwise write masks are also present for EL2.

This feature is supported in AArch64 state only.

FEAT\_SRMASK is OPTIONAL from Armv9.5.

FEAT\_SRMASK is mandatory from Armv9.6.

If FEAT\_SRMASK is implemented, then FEAT\_E2H0 is not implemented.

The following field identifies the presence of FEAT\_SRMASK:

- ID\_AA64MMFR4\_EL1.SRMASK.

## FEAT\_SSVE\_AES, Streaming SVE Mode Advanced Encryption Standard and 128-bit polynomial multiply long instructions

FEAT\_SSVE\_AES implements the SVE AES and 128-bit polynomial multiply long instructions, identified as implemented by ID\_AA64ZFR0\_EL1.AES field, when the PE is in Streaming SVE mode.

This feature is supported in AArch64 state only.

FEAT\_SSVE\_AES is OPTIONAL from Armv9.5.

If FEAT\_SSVE\_AES is implemented, then FEAT\_SME2p1 is implemented.

The following field identifies the presence of FEAT\_SSVE\_AES:

- ID\_AA64SMFR0\_EL1.AES.

For more information, see:

- 'AES-128 instructions'.
- 'Polynomial arithmetic'.

## FEAT\_SSVE\_BitPerm, Streaming Scalable Vector Bit Permutes instructions

FEAT\_SSVE\_BitPerm implements the SVE2 bit permute instructions, identified as implemented by ID\_AA64ZFR0\_EL1.BitPerm, when the PE is in Streaming SVE mode.

This feature is supported in AArch64 state only.

FEAT\_SSVE\_BitPerm is OPTIONAL from Armv9.4.

If FEAT\_SSVE\_BitPerm is implemented, then FEAT\_SME2p1 is implemented.

When FEAT\_SSVE\_BitPerm and FEAT\_SVE2 is implemented, FEAT\_SVE\_BitPerm is implemented.

The following field identifies the presence of FEAT\_SSVE\_BitPerm:

- ID\_AA64SMFR0\_EL1.SBitPerm.

For more information, see:

- 'Bit permutation'.

## FEAT\_SSVE\_FEXPA, Streaming FEXPA instruction

FEAT\_SSVE\_FEXPA implements the SVE FEXPA instruction when the PE is in Streaming SVE mode.

This feature is supported in AArch64 state only.

FEAT\_SSVE\_FEXPA is OPTIONAL from Armv9.4.

If FEAT\_SSVE\_FEXPA is implemented, then FEAT\_SME2p1 is implemented.

The following field identifies the presence of FEAT\_SSVE\_FEXPA:

- ID\_AA64SMFR0\_EL1.SFEXPA.

## FEAT\_SVE2p2, Scalable Vector Extensions version 2.2

The Scalable Vector Extension version 2.2 (SVE2.2) is a superset of SVE2.1 that adds:

- Floating-point round to integral floating-point value instructions.
- Scalar index of first/last true predicate element.
- Zeroing-predication variant to all SVE unary instructions.
- Additional variants of COMPACT and EXPAND instructions.

This feature is supported in AArch64 state only.

FEAT\_SVE2p2 is OPTIONAL from Armv9.5.

In an Armv9.6 implementation, if FEAT\_SVE2 is implemented, FEAT\_SVE2p2 is implemented.

If FEAT\_SVE2p2 is implemented, then FEAT\_SVE2p1 is implemented.

If FEAT\_SVE2 and FEAT\_SME2p2 are implemented, then FEAT\_SVE2p2 is implemented.

The following field identifies the presence of FEAT\_SVE2p2:

- ID\_AA64ZFR0\_EL1.SVEver.

For more information, see:

- 'Predicate element index'.
- 'Floating-point round'.
- 'Vector permutation'.

## FEAT\_SVE\_AES2, SVEmulti-vector Advanced Encryption Standard and 128-bit polynomial multiply long instructions

FEAT\_SVE\_AES2 implements the SVE multi-vector Advanced Encryption Standard and 128-bit destination element polynomial multiply long instructions, when the PE is not in Streaming SVE mode.

This feature is supported in AArch64 state only.

FEAT\_SVE\_AES2 is OPTIONAL from Armv9.5.

If FEAT\_SVE\_AES2 is implemented, then FEAT\_SVE\_PMULL128 is implemented.

If FEAT\_SVE\_AES2 is implemented, then FEAT\_SVE2p1 or FEAT\_SSVE\_AES is implemented.

The following field identifies the presence of FEAT\_SVE\_AES2:

- ID\_AA64ZFR0\_EL1.AES.

For more information, see:

- 'AES-128 instructions'.
- 'Polynomial arithmetic'.

## FEAT\_SVE\_BFSCALE, BFloat16 Floating-Point Adjust Exponent

FEAT\_SVE\_BFSCALE introduces the following:

- If FEAT\_SVE2 is implemented, the SVE BFSCALE instruction when the PE is not in Streaming SVE mode.
- If FEAT\_SME2 is implemented, the SVE BFSCALE instruction when the PE is in Streaming SVE mode, and the SMEmulti-vector Z-targeting BFloat16 scaling instructions, BFSCALE and BFMUL .

This feature is supported in AArch64 state only.

FEAT\_SVE\_BFSCALE is OPTIONAL from Armv9.2.

If FEAT\_SVE\_BFSCALE is implemented, then FEAT\_SVE\_B16B16 is implemented.

The following field identifies the presence of FEAT\_SVE\_BFSCALE:

- ID\_AA64ZFR0\_EL1.B16B16.

For more information, see:

- For SVE: 'Floating-point adjust exponent'.
- For SME: 'Floating-point adjust exponent'.

## FEAT\_SVE\_F16F32MM, SVE Half-precision floating-point matrix multiply-accumulate to single-precision

FEAT\_SVE\_F16F32MM introduces the SVE half-precision floating-point matrix multiply-accumulate to single-precision instruction.

This feature is supported in AArch64 state only.

FEAT\_SVE\_F16F32MM is OPTIONAL from Armv9.2.

If FEAT\_SVE\_F16F32MM is implemented, then FEAT\_SVE2p1 is implemented.

The following field identifies the presence of FEAT\_SVE\_F16F32MM:

- ID\_AA64ZFR0\_EL1.F16MM.

For more information, see:

- 'Floating-point matrix multiply-accumulate'.

## FEAT\_TRBE\_EXC, Trace Buffer Profiling exception extension

FEAT\_TRBE\_EXC provides support for reporting trace buffer management events as TRBE Profiling exceptions.

This feature is supported in AArch64 state only.

FEAT\_TRBE\_EXC is OPTIONAL from Armv9.5.

If FEAT\_TRBE\_EXC is implemented, then FEAT\_TRBEv1p1 is implemented.

The following field identifies the presence of FEAT\_TRBE\_EXC:

- ID\_AA64DFR2\_EL1.TRBE\_EXC.

## FEAT\_TRBEv1p1, Trace Buffer Extension version 1.1

FEAT\_TRBEv1p1 introduces the following to the Trace Buffer Extension:

- If EL2 and FEAT\_FGT are implemented, a fine-grained trap on the TSB CSYNC instruction.
- If EL2 is implemented, an EL2 control to override TRBLIMITR\_EL1.nVM.
- Support for the TRBE Profiling exception extension, FEAT\_TRBE\_EXC.

This feature is supported in AArch64 state only.

FEAT\_TRBEv1p1 is OPTIONAL from Armv9.5.

In an Armv9.6 implementation, if FEAT\_TRBE is implemented, FEAT\_TRBEv1p1 is implemented.

If FEAT\_TRBEv1p1 is implemented, then FEAT\_TRBE is implemented.

If FEAT\_TRBEv1p1 is implemented, then FEAT\_TRBE\_EXC is implemented.

The following fields identify the presence of FEAT\_TRBEv1p1:

- ID\_AA64DFR0\_EL1.TraceBuffer.
- TRBDEVARCH.REVISION.

## FEAT\_UINJ, Injection of Undefined Instruction exceptions

FEAT\_UINJ introduces support for software injection of Undefined Instruction exceptions.

This feature is supported in AArch64 state only.

FEAT\_UINJ is OPTIONAL from Armv9.0.

FEAT\_UINJ is mandatory from Armv9.6.

The following field identifies the presence of FEAT\_UINJ:

- ID\_AA64PFR2\_EL1.UINJ.