## A2.2 Armv8-A architecture extensions

## A2.2.1 The Armv8.0 architecture extension

The original Armv8-A architecture is called Armv8.0. It contains mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv8.0 compliant if it includes all of the Armv8.0 architectural features that are mandatory.

An Armv8.0 compliant implementation can additionally include:

- Armv8.0 features that are optional.
- Any arbitrary subset of the architectural features of Armv8.1, subject only to those constraints that require that certain features be implemented together.

## FEAT\_AA32, PE supports AArch32.

FEAT\_AA32 is OPTIONAL.

If FEAT\_AA32 is implemented, then FEAT\_AA32EL0 is implemented.

## FEAT\_AA32EL0, Support for AArch32 at EL0

FEAT\_AA32EL0 is OPTIONAL from Armv8.0.

If FEAT\_AA32EL0 is implemented, then FEAT\_EL0 is implemented.

If FEAT\_AA32EL0 is implemented, then FEAT\_AA32 is implemented.

## FEAT\_AA32EL1, Support for AArch32 at EL1

FEAT\_AA32EL1 is OPTIONAL from Armv8.0.

If Armv9.0 is implemented, then FEAT\_AA32EL1 is not implemented.

If FEAT\_AA32EL1 is implemented, then FEAT\_AA32EL0 is implemented.

If FEAT\_AA32EL1 is implemented, then FEAT\_EL1 is implemented.

## FEAT\_AA32EL2, Support for AArch32 at EL2

FEAT\_AA32EL2 is OPTIONAL from Armv8.0.

If FEAT\_AA32EL2 is implemented, then FEAT\_AA32EL1 is implemented.

If FEAT\_AA32EL2 is implemented, then FEAT\_EL2 is implemented.

## FEAT\_AA32EL3, Support for AArch32 at EL3

FEAT\_AA32EL3 is OPTIONAL from Armv8.0.

If FEAT\_AA32EL3 is implemented, then FEAT\_AA32EL1 is implemented.

When FEAT\_AA32EL3 and FEAT\_EL2 are implemented, FEAT\_AA32EL2 is implemented.

If FEAT\_AA32EL3 is implemented, then FEAT\_EL3 is implemented.

## FEAT\_AA64, PE uses AArch64 after last reboot

FEAT\_AA64 is OPTIONAL from Armv8.0.

If FEAT\_AA64 is implemented, then FEAT\_AA64EL0, FEAT\_AA64EL1, FEAT\_AA64EL2, or FEAT\_AA64EL3 is implemented.

When FEAT\_AA64EL0, FEAT\_AA64EL1, FEAT\_AA64EL2, or FEAT\_AA64EL3 is implemented, FEAT\_AA64 is implemented.

## FEAT\_AA64EL0, Support for AArch64 at EL0

FEAT\_AA64EL0 is OPTIONAL from Armv8.0.

FEAT\_AA64EL0 is mandatory from Armv9.0.

If FEAT\_AA64EL0 is implemented, then FEAT\_AA64EL1 is implemented.

If FEAT\_AA64EL0 is implemented, then FEAT\_EL0 is implemented.

## FEAT\_AA64EL1, Support for AArch64 at EL1

FEAT\_AA64EL1 is OPTIONAL from Armv8.0.

FEAT\_AA64EL1 is mandatory from Armv9.0.

If FEAT\_AA64EL1 is implemented, then FEAT\_AA64EL0 is implemented.

When FEAT\_AA64EL1 and FEAT\_EL2 are implemented, FEAT\_AA64EL2 is implemented.

When FEAT\_AA64EL1 and FEAT\_EL3 are implemented, FEAT\_AA64EL3 is implemented.

If FEAT\_AA64EL1 is implemented, then FEAT\_EL1 is implemented.

## FEAT\_AA64EL2, Support for AArch64 at EL2

FEAT\_AA64EL2 is OPTIONAL from Armv8.0.

If FEAT\_AA64EL2 is implemented, then FEAT\_AA64EL1 is implemented.

When FEAT\_AA64EL2 and FEAT\_EL3 are implemented, FEAT\_AA64EL3 is implemented.

If FEAT\_AA64EL2 is implemented, then FEAT\_EL2 is implemented.

## FEAT\_AA64EL3, Support for AArch64 at EL3

FEAT\_AA64EL3 is OPTIONAL from Armv8.0.

If FEAT\_AA64EL3 is implemented, then FEAT\_AA64EL1 is implemented.

When FEAT\_AA64EL3 and FEAT\_EL2 are implemented, FEAT\_AA64EL2 is implemented.

If FEAT\_AA64EL3 is implemented, then FEAT\_EL3 is implemented.

## FEAT\_AES, Advanced SIMD AES instructions

FEAT\_AES provides the AES* instructions to support AES encryption and decryption, AESD, AESE, AESMC, and AESIMC.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_AES is OPTIONAL from Armv8.0.

If FEAT\_AES is implemented, then FEAT\_Crypto is implemented.

The following field identifies the presence of FEAT\_AES:

- ID\_AA64ISAR0\_EL1.AES.

## FEAT\_ASID16, 16 bit ASID

FEAT\_ASID16 is OPTIONAL from Armv8.0.

The following field identifies the presence of FEAT\_ASID16:

- ID\_AA64MMFR0\_EL1.ASIDBits.

## FEAT\_AdvSIMD, Advanced SIMD Extension

FEAT\_AdvSIMD includes support for the SISD and SIMD operations. All Armv8-A systems that support standard operating systems with rich application environments also provide hardware support for Advanced SIMD instructions.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_AdvSIMD is OPTIONAL from Armv8.0.

If FEAT\_AdvSIMD is implemented, then FEAT\_FP is implemented.

The following fields identify the presence of FEAT\_AdvSIMD:

- ID\_AA64PFR0\_EL1.AdvSIMD.
- EDPFR.AdvSIMD.

For more information, see:

- Supported data types.
- A64 Advanced SIMD and Floating-point Instruction Descriptions.
- Advanced SIMD and floating-point instructions.
- T32 and A32 Advanced SIMD and Floating-point Instruction Descriptions.

## FEAT\_BigEnd, Support for big-endian at EL1 and above

FEAT\_BigEnd is OPTIONAL from Armv8.0.

If FEAT\_BigEnd is implemented, then FEAT\_BigEndEL0 is implemented.

If FEAT\_MixedEnd is implemented, then FEAT\_BigEnd is implemented.

## FEAT\_BigEndEL0, Support for big-endian at EL0

FEAT\_BigEndEL0 is OPTIONAL from Armv8.0.

If FEAT\_MixedEndEL0 is implemented, then FEAT\_BigEndEL0 is implemented.

## FEAT\_CRC32, CRC32 instructions

FEAT\_CRC32 introduces the support for the CRC32* instructions that perform cyclic redundancy check calculations.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_CRC32 is OPTIONAL from Armv8.0.

FEAT\_CRC32 is mandatory from Armv8.1.

The following fields identify the presence of FEAT\_CRC32:

- ID\_AA64ISAR0\_EL1.CRC32.
- ID\_ISAR5\_EL1.CRC32.
- ID\_ISAR5.CRC32.

## FEAT\_CSV2, Cache Speculation Variant 2

FEAT\_CSV2 introduces a mechanism to identify if hardware cannot disclose information about whether any prediction resource, such as branch target, data-value, or cache prefetch, trained in one hardware described context can control speculative execution in a different hardware described context.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_CSV2 is OPTIONAL from Armv8.0.

FEAT\_CSV2 is mandatory from Armv8.5.

The following fields identify the presence of FEAT\_CSV2:

- ID\_AA64PFR0\_EL1.CSV2.
- ID\_PFR0\_EL1.CSV2.
- ID\_PFR0.CSV2.

For more information, see:

- For AArch64, 'Restrictions on the effects of speculation'.
- 'AArch32 restrictions on the effects of speculation'.

## FEAT\_CSV2\_1p1, Cache Speculation Variant 2

For FEAT\_CSV2\_1p1, within a hardware-described context, branch targets trained for branches situated at one address can control speculative execution of branches situated at different addresses only in a hard-to-determine way.

FEAT\_CSV2\_1p1 does not support the SCXTNUM\_ELx registers.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_CSV2\_1p1 is OPTIONAL from Armv8.0.

If FEAT\_CSV2\_1p1 is implemented, then FEAT\_CSV2 is implemented.

The following fields identify the presence of FEAT\_CSV2\_1p1:

- ID\_AA64PFR1\_EL1.CSV2\_frac.
- ID\_AA64PFR0\_EL1.CSV2.
- ID\_PFR0\_EL1.CSV2.
- ID\_PFR0.CSV2.

For more information, see:

- For AArch64, 'Restrictions on the effects of speculation'.
- 'AArch32 restrictions on the effects of speculation'.

## FEAT\_CSV2\_1p2, Cache Speculation Variant 2 version 1.2

For FEAT\_CSV2\_1p2, within a hardware-described context, branch targets trained for branches situated at one address can control speculative execution of branches situated at different addresses only in a hard-to-determine way.

FEAT\_CSV2\_1p2 introduces the SCXTNUM\_ELx registers, but the contexts do not include the SCXTNUM\_ELx register contexts.

This feature is supported in AArch64 state only.

FEAT\_CSV2\_1p2 is OPTIONAL from Armv8.0.

If FEAT\_CSV2\_1p2 is implemented, then FEAT\_CSV2\_1p1 is implemented.

The following fields identify the presence of FEAT\_CSV2\_1p2:

- ID\_AA64PFR1\_EL1.CSV2\_frac.
- ID\_AA64PFR0\_EL1.CSV2.

For more information, see:

- For AArch64, 'Restrictions on the effects of speculation'.
- 'AArch32 restrictions on the effects of speculation'.

## FEAT\_CSV2\_2, Cache Speculation Variant 2 version 2

FEAT\_CSV2\_2 introduces the SCXTNUM\_ELx registers, which provide a number that can be used to separate out different context numbers within their respective Exception levels for the purpose of protecting against speculative attacks through prediction resources.

This feature is supported in AArch64 state only.

FEAT\_CSV2\_2 is OPTIONAL from Armv8.0.

If FEAT\_CSV2\_2 is implemented, then FEAT\_CSV2 is implemented.

If FEAT\_CSV2\_2 is implemented, then FEAT\_CSV2\_1p1 is not implemented.

The following field identifies the presence of FEAT\_CSV2\_2:

- ID\_AA64PFR0\_EL1.CSV2.

For more information, see:

- For AArch64, 'Restrictions on the effects of speculation'.
- 'AArch32 restrictions on the effects of speculation'.

## FEAT\_CSV2\_3, Cache Speculation Variant 2 version 3

FEAT\_CSV2\_3 introduces a mechanism to identify if hardware cannot disclose information about whether prediction resources based on branch history trained in one hardware described context can control speculative execution in a different hardware described context.

This feature is supported in AArch64 state only.

FEAT\_CSV2\_3 is OPTIONAL from Armv8.0.

If FEAT\_CSV2\_3 is implemented, then FEAT\_CSV2\_2 is implemented.

The following field identifies the presence of FEAT\_CSV2\_3:

- ID\_AA64PFR0\_EL1.CSV2.

For more information, see:

- For AArch64, 'Restrictions on the effects of speculation'.
- 'AArch32 restrictions on the effects of speculation'.

## FEAT\_Crypto, Cryptographic Extension

The Arm Cryptographic Extension provides instructions for the acceleration of encryption and decryption. The presence of the Cryptographic Extension in an implementation is subject to export license controls.

The Cryptographic Extension is an extension of the SIMD support and operates on the vector register file. It also provides multiply instructions that operate on long polynomials.

In an implementation that supports both AArch64 state and AArch32 state, FEAT\_AES, FEAT\_PMULL, FEAT\_SHA1 and FEAT\_SHA256 provide the same functionality in both states.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_Crypto is OPTIONAL.

If FEAT\_Crypto is implemented, then FEAT\_AES or FEAT\_SHA1 is implemented.

In an Armv8.2 implementation, if FEAT\_Crypto is implemented, FEAT\_PMULL, FEAT\_SHA256, FEAT\_SM3, or FEAT\_SM4 is implemented.

For more information, see:

- The Cryptographic Extension in AArch64 state.
- The Cryptographic Extension in AArch32 state.

## FEAT\_DoubleLock, Double Lock

FEAT\_DoubleLock is the mnemonic used for the OS Double Lock.

FEAT\_DoubleLock is OPTIONAL from Armv8.0.

If Armv9.0 is implemented, then FEAT\_DoubleLock is not implemented.

The following fields identify the presence of FEAT\_DoubleLock:

- ID\_AA64DFR0\_EL1.DoubleLock.
- DBGDEVID.DoubleLock.

## FEAT\_EL0, Support for execution at EL0

FEAT\_EL0 is mandatory from Armv8.0.

If FEAT\_EL0 is implemented, then FEAT\_AA32EL0 or FEAT\_AA64EL0 is implemented.

## FEAT\_EL1, Support for execution at EL1

FEAT\_EL1 is mandatory from Armv8.0.

If FEAT\_EL1 is implemented, then FEAT\_AA32EL1 or FEAT\_AA64EL1 is implemented.

## FEAT\_EL2, Support for execution at EL2

FEAT\_EL2 is OPTIONAL from Armv8.0.

If FEAT\_EL2 is implemented, then FEAT\_AA32EL2 or FEAT\_AA64EL2 is implemented.

## FEAT\_EL3, Support for EL3

FEAT\_EL3 is OPTIONAL from Armv8.0.

If FEAT\_EL3 is implemented, then FEAT\_AA32EL3 or FEAT\_AA64EL3 is implemented.

## FEAT\_ETMv4, Embedded Trace Macrocell version 4

FEAT\_ETMv4 indicates support for the Embedded Trace Macrocell architecture ETMv4.

FEAT\_ETMv4 is OPTIONAL from Armv8.0.

If Armv9.0 is implemented, then FEAT\_ETMv4 is not implemented.

If FEAT\_ETMv4 is implemented, then FEAT\_TRC\_SR or FEAT\_TRC\_EXT is implemented.

For more information, see the Arm® Embedded Trace Macrocell Architecture Specification, ETMv4(ARM IHI 0064).

## FEAT\_ETS2, Enhanced Translation Synchronization

FEAT\_ETS2 introduces support for enhanced memory access ordering requirements for translation table walks.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_ETS2 is OPTIONAL from Armv8.0.

FEAT\_ETS2 is mandatory from Armv8.8.

The following fields identify the presence of FEAT\_ETS2:

- ID\_AA64MMFR1\_EL1.ETS.
- ID\_MMFR5\_EL1.ETS.
- ID\_MMFR5.ETS.

For more information, see:

- Ordering requirements defined by the formal concurrency model.
- Ordering of memory accesses from translation table walks.
- Ordering of translation table walks.

## FEAT\_FP, Floating Point extensions

FEAT\_FP includes support for single-precision and double-precision floating-point types. All Armv8-A systems that support standard operating systems with rich application environments also provide hardware support for floating-point instructions.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_FP is OPTIONAL from Armv8.0.

If FEAT\_FP is implemented, then FEAT\_AdvSIMD is implemented.

The following fields identify the presence of FEAT\_FP:

- ID\_AA64PFR0\_EL1.FP.
- EDPFR.FP.

For more information, see:

- Supported data types.
- Floating-point support.
- A64 Advanced SIMD and Floating-point Instruction Descriptions.
- Advanced SIMD and floating-point instructions.
- T32 and A32 Advanced SIMD and Floating-point Instruction Descriptions.

## FEAT\_IVIPT, The IVIPT Extension

FEAT\_IVIPT describes any permitted instruction cache implementation. This includes Virtual Index, Physical tag (VIPT) cache policy and Physical Index, Physical Tag (PIPT) cache policy.

FEAT\_IVIPT is mandatory from Armv8.0.

For more information, see:

- Instruction caches.
- Instruction caches.

## FEAT\_LittleEnd, Support for little-endian at EL1 and above

FEAT\_LittleEnd is OPTIONAL from Armv8.0.

If FEAT\_LittleEnd is implemented, then FEAT\_LittleEndEL0 is implemented.

If FEAT\_MixedEnd is implemented, then FEAT\_LittleEnd is implemented.

## FEAT\_LittleEndEL0, Support for little-endian at EL0

FEAT\_LittleEndEL0 is OPTIONAL from Armv8.0.

If FEAT\_MixedEndEL0 is implemented, then FEAT\_LittleEndEL0 is implemented.

## FEAT\_MixedEnd, Mixed-endian support

FEAT\_MixedEnd provides support for mixed-endian configuration.

FEAT\_MixedEnd is OPTIONAL from Armv8.0.

If FEAT\_MixedEnd is implemented, then FEAT\_MixedEndEL0 is implemented.

The following field identifies the presence of FEAT\_MixedEnd:

- ID\_AA64MMFR0\_EL1.BigEnd.

For more information, see:

- Mixed-endian support in AArch64.
- Mixed-endian support in AArch32.

## FEAT\_MixedEndEL0, Mixed-endian support at EL0

FEAT\_MixedEndEL0 provides support for mixed-endian at EL0.

FEAT\_MixedEndEL0 is OPTIONAL from Armv8.0.

The following fields identify the presence of FEAT\_MixedEndEL0:

- ID\_AA64MMFR0\_EL1.BigEndEL0.
- ID\_AA64MMFR0\_EL1.BigEnd.

For more information, see:

- Mixed-endian support in AArch64.
- Mixed-endian support in AArch32.

## FEAT\_PCSRv8, PC Sample-based Profiling extension

FEAT\_PCSRv8 introduces support for PC Sample-based Profiling Extension that provides coarse-grained, non-invasive profiling by an external debugger.

FEAT\_PCSRv8 is OPTIONAL from Armv8.0.

If FEAT\_PCSRv8 is implemented, then FEAT\_PCSRv8p2 is not implemented.

The following fields identify the presence of FEAT\_PCSRv8:

- DBGDEVID.PCSample.
- DBGDEVID1.PCSROffset.
- EDDEVID1.PCSROffset.
- EDDEVID.PCSample.

For more information, see About the PC Sample-based Profiling Extension.

## FEAT\_PMULL, Advanced SIMD PMULL instructions

FEAT\_PMULL provides the AES* instructions that support multiplication of 64-bit polynomials, PMULL, PMULL2.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_PMULL is OPTIONAL from Armv8.0.

If FEAT\_PMULL is implemented, then FEAT\_AES is implemented.

The following field identifies the presence of FEAT\_PMULL:

- ID\_AA64ISAR0\_EL1.AES.

## FEAT\_PMUv3, PMU extension version 3

The Performance Monitors Extension, FEAT\_PMUv3, is an optional non-invasive debug component.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_PMUv3 is OPTIONAL from Armv8.0.

The following fields identify the presence of FEAT\_PMUv3:

- ID\_AA64DFR0\_EL1.PMUVer.
- ID\_DFR0\_EL1.PerfMon.
- ID\_DFR0.PerfMon.
- EDDFR.PMUVer.

For more information, see The Performance Monitors Extension.

## FEAT\_PMUv3\_EXT, External interface to the Performance Monitors

FEAT\_PMUv3\_EXT indicates support for external access to the FEAT\_PMUv3 and/or FEAT\_PCSRv8p2 registers.

FEAT\_PMUv3\_EXT is OPTIONAL from Armv8.0.

If FEAT\_PMUv3\_EXT is implemented, then FEAT\_PMUv3 or FEAT\_PCSRv8p2 is implemented.

If FEAT\_PMUv3\_EXT is implemented, then FEAT\_PMUv3\_EXT32 or FEAT\_PMUv3\_EXT64 is implemented.

## FEAT\_PMUv3\_EXT32, 32-bit external interface to the Performance Monitors

FEAT\_PMUv3\_EXT32 indicates the external Performance Monitors and CoreSight registers are implemented as mostly 32-bit registers.

FEAT\_PMUv3\_EXT32 is OPTIONAL from Armv8.0.

If FEAT\_PMUv3\_EXT32 is implemented, then FEAT\_PMUv3\_EXT is implemented.

If FEAT\_PMUv3\_EXT32 is implemented, then FEAT\_PMUv3\_EXT64 is not implemented.

The following field identifies the presence of FEAT\_PMUv3\_EXT32:

- PMDEVARCH.ARCHPART.

For more information, see Recommended External Interface to the Performance Monitors.

## FEAT\_SHA1, Advanced SIMD SHA1 instructions

FEAT\_SHA1 implements the SHA1* instructions.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_SHA1 is OPTIONAL from Armv8.0.

If FEAT\_SHA1 is implemented, then FEAT\_Crypto is implemented.

The following field identifies the presence of FEAT\_SHA1:

- ID\_AA64ISAR0\_EL1.SHA1.

## FEAT\_SHA256, Advanced SIMD SHA256 instructions

FEAT\_SHA256 implements the SHA256* instructions.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_SHA256 is OPTIONAL from Armv8.0.

If FEAT\_SHA256 is implemented, then FEAT\_SHA1 is implemented.

The following field identifies the presence of FEAT\_SHA256:

- ID\_AA64ISAR0\_EL1.SHA2.

## FEAT\_Secure, Support for Secure state

FEAT\_Secure adds support for Secure state.

This feature is not supported if EL2 is using AArch32.

FEAT\_Secure is OPTIONAL from Armv8.0.

If FEAT\_RME is not implemented and FEAT\_EL3 is implemented, then FEAT\_Secure is implemented.

## FEAT\_SpecSEI, SError interrupt exceptions from speculative reads of memory

Describes whether the PE can generate SError interrupt exceptions from speculative reads of memory, including speculative instruction fetches.

FEAT\_SpecSEI is OPTIONAL from Armv8.0.

The following fields identify the presence of FEAT\_SpecSEI:

- ID\_AA64MMFR1\_EL1.SpecSEI.
- ID\_MMFR4\_EL1.SpecSEI.
- ID\_MMFR4.SpecSEI.

## FEAT\_TGran16K, Support for 16KB memory translation granule size at stage 1

FEAT\_TGran16K is OPTIONAL from Armv8.0.

When FEAT\_AA64EL2 and FEAT\_TGran16K are implemented, FEAT\_S2TGran16K is implemented.

The following field identifies the presence of FEAT\_TGran16K:

- ID\_AA64MMFR0\_EL1.TGran16.

## FEAT\_TGran4K, Support for 4KB memory translation granule size at stage 1

FEAT\_TGran4K is OPTIONAL from Armv8.0.

When FEAT\_AA64EL2 and FEAT\_TGran4K are implemented, FEAT\_S2TGran4K is implemented.

The following field identifies the presence of FEAT\_TGran4K:

- ID\_AA64MMFR0\_EL1.TGran4.

## FEAT\_TGran64K, Support for 64KB memory translation granule size at stage 1

FEAT\_TGran64K is OPTIONAL from Armv8.0.

When FEAT\_AA64EL2 and FEAT\_TGran64K are implemented, FEAT\_S2TGran64K is implemented.

The following field identifies the presence of FEAT\_TGran64K:

- ID\_AA64MMFR0\_EL1.TGran64.

## FEAT\_TRC\_EXT, Trace external registers

FEAT\_TRC\_EXT indicates support for external access to the ETMv4 or ETE registers.

FEAT\_TRC\_EXT is OPTIONAL from Armv8.0.

If FEAT\_TRC\_EXT is implemented, then FEAT\_ETMv4 or FEAT\_ETE is implemented.

## FEAT\_TRC\_SR, Trace System registers

FEAT\_TRC\_SR indicates support for System registers for ETMv4 or ETE.

This feature is supported in both AArch64 and AArch32, but only when either of these are supported at EL1.

FEAT\_TRC\_SR is OPTIONAL from Armv8.0.

If FEAT\_TRC\_SR is implemented, then FEAT\_ETMv4 or FEAT\_ETE is implemented.

The following fields identify the presence of FEAT\_TRC\_SR:

- ID\_AA64DFR0\_EL1.TraceVer.
- EDDFR.TraceVer.
- ID\_DFR0.CopTrc.
- ID\_DFR0\_EL1.CopTrc.

## FEAT\_nTLBPA, Intermediate caching of translation table walks

FEAT\_nTLBPA introduces a mechanism to identify if the intermediate caching of translation table walks does not include non-coherent caches of previous valid translation table entries since the last completed TLBI applicable to the PE.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_nTLBPA is OPTIONAL from Armv8.0.

The following fields identify the presence of FEAT\_nTLBPA:

- ID\_AA64MMFR1\_EL1.nTLBPA.
- ID\_MMFR5\_EL1.nTLBPA.
- ID\_MMFR5.nTLBPA.

For more information, see:

- TLB maintenance.
- General TLB maintenance requirements.

## A2.2.1.1 Features added to the Armv8.0 extension in later releases

- FEAT\_CHK.
- FEAT\_CLRBHB.
- FEAT\_CP15SDISABLE2.
- FEAT\_CSV3.
- FEAT\_DGH.
- FEAT\_ECBHB.
- FEAT\_ETS3.
- FEAT\_GTG.
- FEAT\_PRFMSLC.
- FEAT\_RAS.
- FEAT\_RPRFM.
- FEAT\_SB.
- FEAT\_SCTLR2.
- FEAT\_SPECRES2.
- FEAT\_SPECRES.
- FEAT\_SSBS2.
- FEAT\_SSBS.
- FEAT\_TCR2.

## A2.2.2 The Armv8.1 architecture extension

The Armv8.1 architecture extension is an extension to Armv8.0. It adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv8.1 compliant if all of the following apply:

- It is Armv8.0 compliant.
- It includes all of the Armv8.1 architectural features that are mandatory.

An Armv8.1 compliant implementation can additionally include:

- Armv8.1 features that are optional.
- Any arbitrary subset of the architectural features of Armv8.2, subject only to those constraints that require that certain features be implemented together.

## FEAT\_Debugv8p1, Debug v8.1

FEAT\_Debugv8p1 is OPTIONAL from Armv8.0.

The following fields identify the presence of FEAT\_Debugv8p1:

- ID\_AA64DFR0\_EL1.DebugVer.
- ID\_DFR0\_EL1.CopDbg.
- ID\_DFR0.CopDbg.
- EDDEVARCH.ARCHVER.

## FEAT\_E2H0, Programming of HCR\_EL2.E2H

When FEAT\_VHE is implemented, FEAT\_E2H0 indicates that HCR\_EL2.E2H can be programmed to the value 0. The absence of FEAT\_E2H0 results in a relaxed behavior where HCR\_EL2.E2H is RES1, with EL2 host mode always enabled.

This feature is supported in AArch64 state only.

FEAT\_E2H0 is OPTIONAL from Armv8.0.

If FEAT\_E2H0 is implemented, then FEAT\_VHE is implemented.

The following field identifies the presence of FEAT\_E2H0:

- ID\_AA64MMFR4\_EL1.E2H0.

## FEAT\_HAFDBS, Hardware management of the Access flag and dirty state

In Armv8.0, all updates to the translation tables are performed by software. From Armv8.1, for the VMSAv8-64 translation regimes only, hardware can perform updates to the translation tables in two contexts:

- Hardware management of the Access flag.
- Hardware management of dirty state, with updates to a dirty state in the translation tables.

The dirty state is introduced in Armv8.1.

Hardware management of dirty state can be enabled only when hardware management of the Access flag is also enabled.

This feature is supported in AArch64 state only.

FEAT\_HAFDBS is OPTIONAL from Armv8.0.

The following field identifies the presence of FEAT\_HAFDBS:

- ID\_AA64MMFR1\_EL1.HAFDBS.

For more information, see:

- Hardware management of the Access flag.
- Hardware management of the dirty state.

## FEAT\_HPDS, Hierarchical permission disables in translations tables

FEAT\_HPDS introduces the facility to disable the hierarchical permissions, APTable, PXNTable, and UXNTable, in the translation tables. This disable has no effect on the NSTable bit.

FEAT\_HPDS is OPTIONAL from Armv8.0.

FEAT\_HPDS is mandatory from Armv8.1.

The following field identifies the presence of FEAT\_HPDS:

- ID\_AA64MMFR1\_EL1.HPDS.

This feature is added only to the VMSAv8-64 translation regimes. Armv8.2 extends this to the AArch32 translation regimes, see FEAT\_AA32HPD.

## FEAT\_LOR, Limited ordering regions

Limited ordering regions allow large systems to perform special Load-Acquire and Store-Release instructions that provide order between the memory accesses to a region of the PA map as observed by a limited set of observers.

This feature is supported in AArch64 state only.

FEAT\_LOR is OPTIONAL from Armv8.0.

FEAT\_LOR is mandatory from Armv8.1.

The following field identifies the presence of FEAT\_LOR:

- ID\_AA64MMFR1\_EL1.LO.

For more information, see Limited ordering regions.

## FEAT\_LSE, Large System Extensions

FEAT\_LSE introduces a set of atomic instructions:

- Compare and Swap instructions, CAS and CASP .
- Atomic memory operation instructions, LD&lt;OP&gt; and ST&lt;OP&gt;, where &lt;OP&gt; is one of ADD, CLR, EOR, SET, SMAX, SMIN, UMAX, and UMIN.
- Swap instruction, SWP.

This feature is supported in AArch64 state only.

FEAT\_LSE is OPTIONAL from Armv8.0.

FEAT\_LSE is mandatory from Armv8.1.

The following field identifies the presence of FEAT\_LSE:

- ID\_AA64ISAR0\_EL1.Atomic.

For more information, see:

- 'Atomic integer memory operations'.
- 'Swap operations'.
- 'Compare and Swap operations'.

## FEAT\_PAN, Privileged access never

FEAT\_PAN introduces a bit to PSTATE. When the value of this PAN state bit is 1, any privileged data access from EL1, or EL2 when the Effective value of HCR\_EL2.E2H is 1, to a virtual memory address that is accessible to data accesses at EL0, generates a Permission fault.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_PAN is OPTIONAL from Armv8.0.

FEAT\_PAN is mandatory from Armv8.1.

The following fields identify the presence of FEAT\_PAN:

- ID\_AA64MMFR1\_EL1.PAN.
- ID\_MMFR3\_EL1.PAN.
- ID\_MMFR3.PAN.

For more information, see:

- PSTATE.PAN.
- About the PAN bit.

## FEAT\_PMUv3p1, Armv8.1 PMU extensions

FEAT\_PMUv3p1 introduces the following:

- The event number space is extended to 16 bits.
- The HPMD bit is added to MDCR\_EL2. This bit disables event counting at EL2.
- The STALL\_FRONTEND and STALL\_BACKEND events are required to be implemented.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_PMUv3p1 is OPTIONAL from Armv8.0.

In an Armv8.1 implementation, if FEAT\_PMUv3 is implemented, FEAT\_PMUv3p1 is implemented.

If FEAT\_PMUv3p1 is implemented, then FEAT\_PMUv3 is implemented.

The following fields identify the presence of FEAT\_PMUv3p1:

- ID\_AA64DFR0\_EL1.PMUVer.
- ID\_DFR0\_EL1.PerfMon.
- ID\_DFR0.PerfMon.
- EDDFR.PMUVer.

For more information, see 'Required events'.

## FEAT\_RDM, Advanced SIMD rounding double multiply-accumulate instructions

FEAT\_RDM introduces Rounding Double Multiply Add/Subtract Advanced SIMD instructions. For more information, see:

For the A64 instruction set

- SQRDMLAH(by element).
- SQRDMLAH(vectors).
- SQRDMLSH(by element).
- SQRDMLSH(vector).

For the T32 and A32 instruction sets

- VQRDMLAH.
- VQRDMLSH.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_RDM is OPTIONAL from Armv8.0.

In an Armv8.1 implementation, if FEAT\_AdvSIMD is implemented, FEAT\_RDM is implemented.

The following fields identify the presence of FEAT\_RDM:

- ID\_AA64ISAR0\_EL1.RDM.
- ID\_ISAR5\_EL1.RDM.
- ID\_ISAR5.RDM.

## FEAT\_VHE, Virtualization Host Extensions

Armv8.1 introduces the Virtualization Host Extensions (VHE) that provide enhanced support for Type 2 hypervisors in Non-secure state.

FEAT\_VHE is OPTIONAL from Armv8.0.

In an Armv8.1 implementation, if FEAT\_AA64EL2 is implemented, FEAT\_VHE is implemented.

If FEAT\_VHE is implemented, then FEAT\_LSE, FEAT\_Debugv8p1, and FEAT\_AA64EL2 are implemented.

The following field identifies the presence of FEAT\_VHE:

- ID\_AA64MMFR1\_EL1.VH.

For more information, see Virtualization Host Extensions

## FEAT\_VMID16, 16-bit VMID

In an Armv8.1 implementation, when EL2 is using AArch64, the virtual machine identifier (VMID) size is an IMPLEMENTATION DEFINED choice of 8 bits or 16 bits.

When implemented, this feature is supported only when EL2 is using AArch64.

FEAT\_VMID16 is OPTIONAL from Armv8.0.

The following field identifies the presence of FEAT\_VMID16:

- ID\_AA64MMFR1\_EL1.VMIDBits.

For more information, see VMID size.

## A2.2.2.1 Features added to the Armv8.1 extension in later releases

- FEAT\_DPB2.
- FEAT\_DotProd.
- FEAT\_FHM.
- FEAT\_FlagM.
- FEAT\_PAN3.

## A2.2.3 The Armv8.2 architecture extension

The Armv8.2 architecture extension is an extension to Armv8.1. It adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv8.2 compliant if all of the following apply:

- It is Armv8.1 compliant.
- It includes all of the Armv8.2 architectural features that are mandatory.

An Armv8.2 compliant implementation can additionally include:

- Armv8.2 features that are optional.
- Any arbitrary subset of the architectural features of Armv8.3, subject only to those constraints that require that certain features be implemented together.

## FEAT\_AA32HPD, AArch32 Hierarchical permission disables

FEAT\_HPDS introduced the ability to disable the hierarchical permissions, APTable, PXNTable, and UXNTable, in the VMSAv8-64 translation regimes. FEAT\_AA32HPD extends this functionality to the VMSAv8-32 translation regimes when those regimes are using the Long descriptor Translation Table format.

This feature is supported in AArch32 state only.

FEAT\_AA32HPD is OPTIONAL from Armv8.1.

If FEAT\_AA32HPD is implemented, then FEAT\_AA32 is implemented.

The following fields identify the presence of FEAT\_AA32HPD:

- ID\_MMFR4\_EL1.HPDS.
- ID\_MMFR4.HPDS.

For more information, see Attribute fields in VMSAv8-32 Long-descriptor translation table format descriptors

## FEAT\_AA32I8MM, AArch32 Int8 matrix multiply-accumulate

FEAT\_AA32I8MM introduces integer matrix multiply-accumulate instructions and dot product instructions.

This feature is supported in AArch32 state only.

FEAT\_AA32I8MM is OPTIONAL from Armv8.1.

If FEAT\_AA32I8MM is implemented, then FEAT\_I8MM is implemented.

If FEAT\_AA32I8MM is implemented, then FEAT\_AA32 is implemented.

The following fields identify the presence of FEAT\_AA32I8MM:

- ID\_ISAR6\_EL1.I8MM.
- ID\_ISAR6.I8MM.

For more information, see:

- Advanced SIMD dot product instructions.
- Advanced SIMD matrix multiply-accumulate instructions.

## FEAT\_ASMv8p2, Armv8.2 changes to the A64 ISA

FEAT\_ASMv8p2 introduces the BFC instruction to the A64 instruction set as an alias of BFM. It also requires that the BFC instruction and the A64 pseudo-instruction REV64 are implemented by assemblers.

In Armv8.0 and Armv8.1, the A64 pseudo-instruction REV64 is OPTIONAL.

FEAT\_ASMv8p2 is OPTIONAL from Armv8.1.

FEAT\_ASMv8p2 is mandatory from Armv8.2.

For more information, see:

- BFC.
- REV64.

## FEAT\_DPB, DC CVAP instruction

FEAT\_DPB introduces a mechanism to identify and manage persistent memory locations in a shared memory hierarchy, including adding the DC CVAP instruction.

This feature is supported in AArch64 state only.

FEAT\_DPB is OPTIONAL from Armv8.1.

FEAT\_DPB is mandatory from Armv8.2.

The following field identifies the presence of FEAT\_DPB:

- ID\_AA64ISAR1\_EL1.DPB.

For more information, see Memory hierarchy.

## FEAT\_Debugv8p2, Debug v8.2

FEAT\_Debugv8p2 provides the following changes:

- If the Core power domain is powered up and DoubleLockStatus() == TRUE, EDPRSR.{DLK,SPD,PU} is only permitted to read {UNKNOWN, 0, 0}.
- The definition of Exception Catch debug events is extended to include reset entry.
- All CONSTRAINED UNPREDICTABLE cases that generate Exception Catch debug events are removed.
- Controls are added to EDECCR to control Exception Catch debug event generation on exception return.
- All IMPLEMENTATION DEFINED control of external debug accesses to OSLAR\_EL1 is removed.
- ExternalSecureNoninvasiveDebugEnabled() cannot override software controls of counting attributable events in Secure state.

FEAT\_Debugv8p2 is OPTIONAL from Armv8.1.

FEAT\_Debugv8p2 is mandatory from Armv8.2.

If FEAT\_Debugv8p2 is implemented, then FEAT\_Debugv8p1 is implemented.

The following fields identify the presence of FEAT\_Debugv8p2:

- ID\_AA64DFR0\_EL1.DebugVer.
- ID\_DFR0\_EL1.CopDbg.
- DBGDIDR.Version.
- ID\_DFR0.CopDbg.
- EDDEVARCH.ARCHVER.

For more information, see:

- Exception Catch debug event.
- EDPRSR.{DLK, SPD, PU} and the Core power domain.
- Interaction with EL3.
- External access disabled.

## FEAT\_F32MM, Single-precision floating-point matrix multiply-accumulate

FEAT\_F32MM introduces support for the SVE single-precision floating-point matrix multiply-accumulate variant of the FMMLAinstruction.

This feature is supported in AArch64 state only.

FEAT\_F32MM is OPTIONAL from Armv8.2.

If FEAT\_F32MM is implemented, then FEAT\_SVE is implemented.

The following field identifies the presence of FEAT\_F32MM:

- ID\_AA64ZFR0\_EL1.F32MM.

## FEAT\_F64MM, Double-precision floating-point matrix multiply-accumulate

FEAT\_F64MM introduces support for the following SVE instructions:

- FMMLA(double-precision floating-point matrix multiply-accumulate variant).
- LD1ROB (scalar plus immediate).
- LD1ROB (scalar plus scalar).
- LD1ROD (scalar plus immediate).
- LD1ROD (scalar plus scalar).
- LD1ROH (scalar plus immediate).
- LD1ROH (scalar plus scalar).
- LD1ROW(scalar plus immediate).
- LD1ROW(scalar plus scalar).
- TRN1, TRN2 (vectors) (128-bit variant).
- UZP1, UZP2 (vectors) (128-bit variant).
- ZIP1, ZIP2 (vectors) (128-bit variant).

This feature is supported in AArch64 state only.

FEAT\_F64MM is OPTIONAL from Armv8.2.

If FEAT\_F64MM is implemented, then FEAT\_SVE is implemented.

The following field identifies the presence of FEAT\_F64MM:

- ID\_AA64ZFR0\_EL1.F64MM.

## FEAT\_FP16, Half-precision floating-point data processing

FEAT\_FP16 supports:

- Half-precision data-processing instructions for Advanced SIMD and floating-point in both AArch64 and AArch32 states.

The following fields enable flushing of denormalized numbers to zero for half-precision data-processing instructions:

- FPCR.FZ16.
- FPSCR.FZ16.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_FP16 is OPTIONAL from Armv8.2.

In an Armv8.4 implementation, if FEAT\_FHM is not implemented, then FEAT\_FP16 is not implemented.

In an Armv8.2 implementation, if FEAT\_SVE or FEAT\_FHM is implemented, FEAT\_FP16 is implemented.

The following fields identify the presence of FEAT\_FP16:

- ID\_AA64PFR0\_EL1.FP.
- ID\_AA64PFR0\_EL1.AdvSIMD.
- MVFR1\_EL1.FPHP.
- MVFR1\_EL1.SIMDHP.
- MVFR1.FPHP.
- MVFR1.SIMDHP.

For more information, see:

- Half-precision floating-point formats.
- Flushing denormalized numbers to zero.
- Modified immediate constants in A64 floating-point instructions.

## FEAT\_HPDS2, Hierarchical permission disables

FEAT\_HPDS2 provides a mechanism to allow operating systems or hypervisors to make up to four bits of Translation Table final-level descriptors available for IMPLEMENTATION DEFINED hardware use.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_HPDS2 is OPTIONAL from Armv8.1.

When FEAT\_AA32EL1 and FEAT\_HPDS2 are implemented, FEAT\_AA32HPD is implemented.

If FEAT\_HPDS2 is implemented, then FEAT\_HPDS is implemented.

The following fields identify the presence of FEAT\_HPDS2:

- ID\_AA64MMFR1\_EL1.HPDS.
- ID\_MMFR4\_EL1.HPDS.
- ID\_MMFR4.HPDS.

For more information, see:

- Page Based Hardware attributes.
- Attribute fields in VMSAv8-32 Long-descriptor translation table format descriptors.

## FEAT\_I8MM, AArch64 Int8 matrix multiply-accumulate

FEAT\_I8MM introduces integer matrix multiply-accumulate instructions and dot product instructions.

This feature is supported in AArch64 state only.

FEAT\_I8MM is OPTIONAL from Armv8.1.

FEAT\_I8MM is mandatory from Armv8.6.

The following fields identify the presence of FEAT\_I8MM:

- ID\_AA64ISAR1\_EL1.I8MM.
- ID\_AA64ZFR0\_EL1.I8MM.

For more information, see:

- SIMD integer dot product.
- SIMD integer matrix multiply-accumulate.
- SVE Integer dot product.
- SVE Integer matrix multiply operations.

## FEAT\_IESB, Implicit Error Synchronization event

FEAT\_IESB introduces control for an implicit error synchronization event at exception entry and return.

The implicit error synchronization events affect the same synchronizable asynchronous events that are synchronized by the ESB instruction. This means that if an implementation has either no sources of SError exceptions, or all SError exceptions are not synchronizable errors, then the controls added by this feature have no effect.

This feature is supported in AArch64 state only.

FEAT\_IESB is OPTIONAL from Armv8.1.

If FEAT\_IESB is implemented, then FEAT\_RAS is implemented.

The following field identifies the presence of FEAT\_IESB:

- ID\_AA64MMFR2\_EL1.IESB.

For more information, see Error synchronization event.

## FEAT\_LPA, Large PA and IPA support

FEAT\_LPA:

- Allows a larger physical address (PA) and intermediate physical address (IPA) space of up to 52 bits when using the 64KB translation granule.
- Allows a level 1 block size where the block covers a 4TB address range for the 64KB translation granule if the implementation support 52 bits of PA.

This feature is supported in AArch64 state only.

FEAT\_LPA is OPTIONAL from Armv8.1.

The following field identifies the presence of FEAT\_LPA:

- ID\_AA64MMFR0\_EL1.PARange.

For more information about FEAT\_LPA, see:

- Implemented physical address size.
- Output address size configuration.
- Intermediate physical address size configuration
- Translation using the 64KB granule
- Table descriptor format
- Block descriptor and Page descriptor formats

## FEAT\_LSMAOC, AArch32 Load/Store Multiple instruction atomicity and ordering controls

FEAT\_LSMAOC introduces controls that disable legacy behavior of AArch32 load multiple and store multiple instructions, and provide a trap of one aspect of this legacy behavior.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_LSMAOC is OPTIONAL from Armv8.1.

If FEAT\_LSMAOC is implemented, then FEAT\_AA32 is implemented.

The following fields identify the presence of FEAT\_LSMAOC:

- ID\_AA64MMFR2\_EL1.LSM.
- ID\_MMFR4\_EL1.LSM.
- ID\_MMFR4.LSM.

For more information, see the register field descriptions and:

- Generation of Alignment faults by load/store multiple accesses to Device memory.
- Multi-register loads and stores that access Device memory.
- Taking an interrupt or other exception during a multiple-register load or store.

## FEAT\_LVA, Large VA support

FEAT\_LVA supports a virtual address (VA) space for each translation table base register of up to 52 bits when using any of the following:

- VMSAv9-128 translation format.
- VMSAv8-64 translation format with the 64KB translation granule.

This feature is supported in AArch64 state only.

FEAT\_LVA is OPTIONAL from Armv8.1.

The following field identifies the presence of FEAT\_LV A:

- ID\_AA64MMFR2\_EL1.VARange.

For more information about FEAT\_LVA, see:

- Supported virtual address ranges.
- Input address size configuration.
- Translation using the 64KB granule.

## FEAT\_PAN2, AT S1E1R and AT S1E1W instruction variants affected by PSTATE.PAN

FEAT\_PAN2 introduces variants of the AArch64 AT S1E1R and AT S1E1W instructions and the AArch32 ATS1CPR and ATS1CPW instructions. These instructions factor in the PSTATE.PAN bit when determining whether or not the location will generate a Permission fault for a privileged access, as is reported in the PAR. For more information, see:

For the AArch64 System instructions:

- AT S1E1RP, Address Translate Stage 1 EL1 Read PAN.
- AT S1E1RP, Address Translate Stage 1 EL1 Write PA.

For the AArch32 System instructions:

- ATS1CPRP, Address Translate Stage 1 Current state PL1 Read PAN.
- ATS1CPRP, Address Translate Stage 1 Current state PL1 write PAN.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_PAN2 is OPTIONAL from Armv8.1.

FEAT\_PAN2 is mandatory from Armv8.2.

If FEAT\_PAN2 is implemented, then FEAT\_PAN is implemented.

The following fields identify the presence of FEAT\_PAN2:

- ID\_AA64MMFR1\_EL1.PAN.
- ID\_MMFR3\_EL1.PAN.
- ID\_MMFR3.PAN.

For more information, see:

- Address translation instructions.
- Address translation instructions.
- ATS1C**, Address translation stage 1, current security state.
- Encoding and availability of the address translation instructions.

## FEAT\_PCSRv8p2, PC Sample-based Profiling Extension

FEAT\_PCSRv8p2 moves the control and implementation of the OPTIONAL PC Sample-based Profiling Extension from the ED*SR Debug registers to PM*SR registers in the Performance Monitors address space.

FEAT\_PCSRv8p2 is OPTIONAL from Armv8.1.

If FEAT\_PCSRv8p2 is implemented, then FEAT\_PCSRv8 is not implemented.

The following field identifies the presence of FEAT\_PCSRv8p2:

- PMDEVID.PCSample.

For more information, see The PC Sample-based Profiling Extension.

## FEAT\_RAS, Reliability, Availability and Serviceability (RAS) Extension

FEAT\_RAS introduces the following:

- The Error Synchronization Barrier (ESB) instruction for the A32, T32, and A64 instruction sets.
- Error records.
- The Error synchronization event.
- Additional syndrome information on External Aborts.

FEAT\_RAS is OPTIONAL from Armv8.0.

FEAT\_RAS is mandatory from Armv8.2.

The following fields identify the presence of FEAT\_RAS:

- ID\_AA64PFR0\_EL1.RAS.
- ID\_PFR0\_EL1.RAS.
- ID\_PFR0.RAS.

For more information, see:

- Reliability, Availability, and Serviceability.
- RAS PE Architecture.
- Arm ® Reliability Availability and Serviceability (RAS) System Architecture, for A-profile architecture (ARM IHI 0100).

## FEAT\_SHA3, Advanced SIMD SHA3 instructions

FEAT\_SHA3 introduces Advanced SIMD instructions that support SHA3 functionality.

These instructions are added to the A64 instruction set only.

FEAT\_SHA3 is OPTIONAL from Armv8.1.

If FEAT\_SHA3 is implemented, then FEAT\_Crypto is implemented.

If FEAT\_SHA3 is implemented, then FEAT\_SHA256 and FEAT\_SHA1 are implemented.

The following field identifies the presence of FEAT\_SHA3:

- ID\_AA64ISAR0\_EL1.SHA3.

For more information, see FEAT\_SHA3, SHA3 functionality.

## FEAT\_SHA512, Advanced SIMD SHA512 instructions

FEAT\_SHA512 introduces Advanced SIMD instructions that support SHA2-512 functionality.

These instructions are added to the A64 instruction set only.

FEAT\_SHA512 is OPTIONAL from Armv8.1.

If FEAT\_SHA512 is implemented, then FEAT\_Crypto is implemented.

If FEAT\_SHA512 is implemented, then FEAT\_SHA256 and FEAT\_SHA1 are implemented.

The following field identifies the presence of FEAT\_SHA512:

- ID\_AA64ISAR0\_EL1.SHA2.

For more information, see FEAT\_SHA512, SHA2-512 functionality.

## FEAT\_SM3, Advanced SIMD SM3 instructions

FEAT\_SM3 introduces Advanced SIMD instructions that support the Chinese cryptography algorithm SM3.

These instructions are added to the A64 instruction set only.

FEAT\_SM3 is OPTIONAL from Armv8.1.

If FEAT\_SM3 is implemented, then FEAT\_Crypto is implemented.

The following field identifies the presence of FEAT\_SM3:

- ID\_AA64ISAR0\_EL1.SM3.

For more information, see FEAT\_SM3, SM3 functionality.

## FEAT\_SM4, Advanced SIMD SM4 instructions

FEAT\_SM4 introduces Advanced SIMD instructions that support the Chinese cryptography algorithm SM4.

These instructions are added to the A64 instruction set only.

FEAT\_SM4 is OPTIONAL from Armv8.1.

If FEAT\_SM4 is implemented, then FEAT\_Crypto is implemented.

The following field identifies the presence of FEAT\_SM4:

- ID\_AA64ISAR0\_EL1.SM4.

For more information, see FEAT\_SM4, SM4 functionality.

## FEAT\_SPE, Statistical Profiling Extension

FEAT\_SPE provides a non-invasive method of sampling software and hardware using randomized sampling of either architectural instructions, as defined by the instruction set architecture, or by microarchitectural operations.

This feature is supported in AArch64 state only.

FEAT\_SPE is OPTIONAL from Armv8.1.

When FEAT\_SPE and FEAT\_PMUv3 are implemented, FEAT\_PMUv3p1 is implemented.

The following field identifies the presence of FEAT\_SPE:

- ID\_AA64DFR0\_EL1.PMSVer.

For more information, see The Statistical Profiling Extension.

## FEAT\_SPE\_ArchInst, Statistical Profiling architectural instruction sampling

FEAT\_SPE\_ArchInst provides sampling of architectural instructions by FEAT\_SPE. If FEAT\_SPE is implemented and FEAT\_SPE\_ArchInst is not implemented, then the PE samples microarchitectural operations.

This feature is supported in AArch64 state only.

FEAT\_SPE\_ArchInst is OPTIONAL.

If FEAT\_SPE\_ArchInst is implemented, then FEAT\_SPE is implemented.

The following field identifies the presence of FEAT\_SPE\_ArchInst:

- PMSIDR\_EL1.ArchInst.

For more information, see The Statistical Profiling Extension.

## FEAT\_SPE\_ERnd, Statistical Profiling random sampling at end of period

FEAT\_SPE\_ERnd provides a secondary counter, PMSICR\_EL1.ECOUNT, that is used after the primary sample counter, PMSICR\_EL1.COUNT, reaches zero when PMSIRR\_EL1.RND is 1. If FEAT\_SPE\_ERnd is not implemented, then bits [7:0] of the primary counter are used to provide a random offset.

This feature is supported in AArch64 state only.

FEAT\_SPE\_ERnd is OPTIONAL.

If FEAT\_SPE\_ERnd is implemented, then FEAT\_SPE is implemented.

The following field identifies the presence of FEAT\_SPE\_ERnd:

- PMSIDR\_EL1.ERnd.

For more information, see The Statistical Profiling Extension.

## FEAT\_SPE\_LDS, Statistical Profiling data source packet generation

FEAT\_SPE\_LDS indicates that the Statistical Profiling Unit (SPU) can generate Data Source packets.

This feature is supported in AArch64 state only.

FEAT\_SPE\_LDS is OPTIONAL.

If FEAT\_SPE\_LDS is implemented, then FEAT\_SPE is implemented.

The following field identifies the presence of FEAT\_SPE\_LDS:

- PMSIDR\_EL1.LDS.

## FEAT\_SVE, Scalable Vector Extension

The Scalable Vector Extension includes the following functionality:

- Configurable vector length with scalable vector lengths from 128 bits up to 2048 bits.
- Predication using scalable predicate registers from 16 bits up to 256 bits.
- Instructions that operate on scalable size vectors and predicates.
- Gather-load and scatter-store.
- Software-managed speculative vectorization.
- System registers and fields to configure the Effective SVE vector length and traps.

The Scalable Vector Extension complements the AArch64 Advanced SIMD and floating-point functionality. SVE does not replace the AArch64 Advanced SIMD and floating-point functionality.

This feature is supported in AArch64 state only.

FEAT\_SVE is OPTIONAL from Armv8.2.

If FEAT\_SVE is implemented, then FEAT\_FCMA and FEAT\_FP16 are implemented.

When FEAT\_SVE and FEAT\_PMUv3 are implemented, FEAT\_PMUv3p1 is implemented.

The following field identifies the presence of FEAT\_SVE:

- ID\_AA64PFR0\_EL1.SVE.

## FEAT\_TTCNP, Translation table Common not private translations

FEAT\_TTCNP permits multiple PEs in the same Inner Shareable domain to use the same translation tables for a given stage of address translation.

This facility is available for all VMSAv8-64 translation regimes and for VMSAv8-32 translation stages that use the Long descriptor Translation Table format.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_TTCNP is OPTIONAL from Armv8.1.

FEAT\_TTCNP is mandatory from Armv8.2.

The following fields identify the presence of FEAT\_TTCNP:

- ID\_AA64MMFR2\_EL1.CnP.
- ID\_MMFR4\_EL1.CnP.
- ID\_MMFR4.CnP.

For more information, see:

- Common not private translations.
- Common not private translations in VMSAv8-32.

## FEAT\_UAO, Unprivileged Access Override control

FEAT\_UAO introduces the UAO bit to PSTATE. When the Effective value of UAO is 1, if memory accesses that are described as unprivileged are made by the unprivileged memory access instructions, they are privileged.

This feature is supported in AArch64 state only.

FEAT\_UAO is OPTIONAL from Armv8.1.

FEAT\_UAO is mandatory from Armv8.2.

The following field identifies the presence of FEAT\_UAO:

- ID\_AA64MMFR2\_EL1.UAO.

For more information, see:

- PSTATE.UAO.
- Load/store unprivileged.
- UAO.

## FEAT\_XNX, Translation table stage 2 Unprivileged Execute-never

FEAT\_XNX extends the stage 2 translation table access permissions to provide control of whether memory is executable at EL0 independent of whether it is executable at EL1.

This facility is available for stage 2 translation stages in VMSAv8-64 and VMSAv8-32.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_XNX is OPTIONAL from Armv8.1.

In an Armv8.2 implementation, if FEAT\_EL2 is implemented, FEAT\_XNX is implemented.

The following fields identify the presence of FEAT\_XNX:

- ID\_AA64MMFR1\_EL1.XNX.
- ID\_MMFR4\_EL1.XNX.
- ID\_MMFR4.XNX.

For more information, see:

- Stage 2 instruction execution using Direct permissions.
- Access permissions for instruction execution.

## A2.2.3.1 Features added to the Armv8.2 extension in later releases

- FEAT\_AA32BF16.
- FEAT\_BF16.
- FEAT\_EBF16.
- FEAT\_EVT.
- FEAT\_LRCPC2.
- FEAT\_LRCPC3.
- FEAT\_LSE2.
- FEAT\_MPAM.
- FEAT\_MPAMv1p0.
- FEAT\_PAuth2.
- FEAT\_RASSAv1p1.
- FEAT\_RASv1p1.

## A2.2.4 The Armv8.3 architecture extension

The Armv8.3 architecture extension is an extension to Armv8.2. It adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv8.3 compliant if all of the following apply:

- It is Armv8.2 compliant.
- It includes all of the Armv8.3 architectural features that are mandatory.

An Armv8.3 compliant implementation can additionally include:

- Armv8.3 features that are optional.
- Any arbitrary subset of the architectural features of Armv8.4, subject only to those constraints that require that certain features be implemented together.

## FEAT\_CCIDX, Extended cache index

FEAT\_CCIDX introduces the following registers to allow caches to be described with greater numbers of sets and greater associativity:

- A64-bit format of CCSIDR\_EL1.
- CCSIDR2\_EL1.
- CCSIDR2.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_CCIDX is OPTIONAL from Armv8.2.

The following fields identify the presence of FEAT\_CCIDX:

- ID\_AA64MMFR2\_EL1.CCIDX.
- ID\_MMFR4\_EL1.CCIDX.
- ID\_MMFR4.CCIDX.

For more information, see:

- Possible formats of the Cache Size Identification Register, CCSIDR\_EL1.
- Possible formats of the Cache Size Identification Register, CCSIDR and CCSIDR2.

## FEAT\_CONSTPACFIELD, PAC algorithm enhancement

FEAT\_CONSTPACFIELD introduces functionality that permits an implementation with pointer authentication to use the value of bit[55] in the virtual address to determine the size of the PAC field when adding a PAC to the virtual address, even when the top byte is not being ignored.

This feature is supported in AArch64 state only.

FEAT\_CONSTPACFIELD is OPTIONAL from Armv8.2.

If FEAT\_CONSTPACFIELD is implemented, then FEAT\_PAuth2 is implemented.

The following field identifies the presence of FEAT\_CONSTPACFIELD:

- ID\_AA64ISAR2\_EL1.PAC\_frac.

For more information, see PAC field.

## FEAT\_DoPD, Debug over Powerdown

FEAT\_DoPD provides a debug programmers' model where all debug and PMU registers are in the Core power domain and all CTI registers are in the Debug power domain. Power control is provided by an OPTIONAL external powerup request mechanism.

When FEAT\_DoPD is implemented:

- The optional Software Lock is not implemented by the architecturally defined debug components in the PE Core power domain.
- If an ETMv4 trace unit is implemented, the ETM must implement:
- ETMv4.2 or later.
- The Unified Power Domain Model.
- If FEAT\_ETE is implemented, the trace unit always implements a single power domain.

FEAT\_DoPD is OPTIONAL from Armv8.2.

If FEAT\_DoPD is implemented, then FEAT\_DoubleLock is not implemented.

If FEAT\_DoPD is implemented, then FEAT\_Debugv8p2 is implemented.

The following field identifies the presence of FEAT\_DoPD:

- EDDEVID.DebugPower.

For more information, see Debug Reset and Powerdown Support.

## FEAT\_EPAC, Enhanced pointer authentication

FEAT\_EPAC introduces functionality that permits setting the Pointer Authentication Code (PAC) field to 0 on performing a PAC operation on a non-canonical address.

This feature is supported in AArch64 state only.

FEAT\_EPAC is OPTIONAL from Armv8.2.

If FEAT\_EPAC is implemented, then FEAT\_PAuth is implemented.

If FEAT\_EPAC is implemented, then FEAT\_PAuth2 is not implemented.

The following fields identify the presence of FEAT\_EPAC:

- ID\_AA64ISAR1\_EL1.APA.
- ID\_AA64ISAR1\_EL1.API.
- ID\_AA64ISAR2\_EL1.APA3.

For more information, see Pointer authentication.

## FEAT\_FCMA, Floating-point complex number instructions

FEAT\_FCMA introduces instructions for floating-point multiplication and addition of complex numbers.

These instructions are added to the A64 and A32/T32 instruction sets.

FEAT\_FCMA is OPTIONAL from Armv8.2.

In an Armv8.3 implementation, if FEAT\_FP is implemented, FEAT\_FCMA is implemented.

If FEAT\_FCMA is implemented, then FEAT\_FP is implemented.

The following fields identify the presence of FEAT\_FCMA:

- ID\_AA64ISAR1\_EL1.FCMA.
- ID\_ISAR5\_EL1.VCMA.
- ID\_ISAR5.VCMA.

For more information, see:

- AArch64 Advanced SIMD complex number arithmetic instructions.
- AArch32 Advanced SIMD complex number arithmetic instructions.

## FEAT\_FPAC, Faulting on AUT* instructions

FEAT\_FPAC introduces faulting on an AUT* instruction.

FEAT\_FPAC is added as a further extension to FEAT\_PAuth2.

This feature is supported in AArch64 state only.

FEAT\_FPAC is OPTIONAL from Armv8.2.

If FEAT\_FPAC is implemented, then FEAT\_PAuth2 is implemented.

The following fields identify the presence of FEAT\_FPAC:

- ID\_AA64ISAR1\_EL1.APA.
- ID\_AA64ISAR1\_EL1.API.
- ID\_AA64ISAR2\_EL1.APA3.

For more information, see Faulting on pointer authentication.

## FEAT\_FPACCOMBINE, Faulting on combined pointer authentication instructions

FEAT\_FPACCOMBINE introduces faulting on the combined instructions that perform pointer authentication.

FEAT\_FPACCOMBINE is added as a further extension to FEAT\_FPAC.

FEAT\_FPACCOMBINE is OPTIONAL from Armv8.2.

If FEAT\_FPACCOMBINE is implemented, then FEAT\_FPAC is implemented.

The following fields identify the presence of FEAT\_FPACCOMBINE:

- ID\_AA64ISAR1\_EL1.APA.
- ID\_AA64ISAR1\_EL1.API.
- ID\_AA64ISAR2\_EL1.APA3.

For more information, see Faulting on pointer authentication.

## FEAT\_FPACC\_SPEC, Speculative behavior of pointer authentication instructions

FEAT\_FPACC\_SPEC introduces consistent impact of speculation for instructions that perform authentication.

FEAT\_FPACC\_SPEC is added as a further extension to FEAT\_FPACCOMBINE.

This feature is supported in AArch64 state only.

FEAT\_FPACC\_SPEC is OPTIONAL from Armv8.2.

If FEAT\_FPACC\_SPEC is implemented, then FEAT\_FPACCOMBINE is implemented.

The following field identifies the presence of FEAT\_FPACC\_SPEC:

- ID\_AA64MMFR3\_EL1.Spec\_FPACC.

For more information, see Faulting on pointer authentication.

## FEAT\_JSCVT, JavaScript conversion instructions

FEAT\_JSCVT introduces JavaScript convert instructions that truncate a double-precision value to a 32-bit signed integer, setting the condition flags to indicate whether the converted value was in range.

These instructions are added to the A64 and A32/T32 instruction sets.

FEAT\_JSCVT is OPTIONAL from Armv8.2.

In an Armv8.3 implementation, if FEAT\_FP is implemented, FEAT\_JSCVT is implemented.

If FEAT\_JSCVT is implemented, then FEAT\_FP is implemented.

The following fields identify the presence of FEAT\_JSCVT:

- ID\_AA64ISAR1\_EL1.JSCVT.
- ID\_ISAR6\_EL1.JSCVT.
- ID\_ISAR6.JSCVT.

For more information, see:

- Floating-point conversion.
- About the A64 Advanced SIMD and floating-point instructions.
- Advanced SIMD and floating-point instructions.
- Floating-point data-processing instructions.

## FEAT\_LRCPC, Load-Acquire RCpc instructions

FEAT\_LRCPC introduces instructions that support the weaker Release Consistency processor consistent (RCpc) model that enables the reordering of a Store-Release followed by a Load-Acquire to a different address.

These instructions are added to the A64 instruction set only.

FEAT\_LRCPC is OPTIONAL from Armv8.2.

FEAT\_LRCPC is mandatory from Armv8.3.

The following field identifies the presence of FEAT\_LRCPC:

- ID\_AA64ISAR1\_EL1.LRCPC.

For more information, see:

- Load-Acquire, Load-AcquirePC, and Store-Release.
- Load-Acquire/Store-Release.

## FEAT\_NV, Nested Virtualization

FEAT\_NV provides support for a Guest Hypervisor to run in EL1 and ensures that the Guest Hypervisor is unaware that it is running at that Exception level. A Guest Hypervisor is supported regardless of the Effective value of HCR\_EL2.E2H.

This feature is supported in AArch64 state only.

FEAT\_NV is OPTIONAL from Armv8.2.

If FEAT\_NV is implemented, then FEAT\_EL2 is implemented.

The following fields identify the presence of FEAT\_NV:

- ID\_AA64MMFR4\_EL1.NV\_frac.
- ID\_AA64MMFR2\_EL1.NV.

For more information, see Nested virtualization.

## FEAT\_PACIMP, Pointer authentication - IMPLEMENTATION DEFINED algorithm

FEAT\_PACIMP permits an IMPLEMENTATION DEFINED cryptographic algorithm to be used for PAC calculation.

This feature is supported in AArch64 state only.

FEAT\_PACIMP is OPTIONAL from Armv8.2.

If FEAT\_PACIMP is implemented, then FEAT\_PAuth is implemented.

If FEAT\_PACIMP is implemented, then FEAT\_PACQARMA5 is not implemented.

If FEAT\_PACIMP is implemented, then FEAT\_PACQARMA3 is not implemented.

The following fields identify the presence of FEAT\_PACIMP:

- ID\_AA64ISAR1\_EL1.GPI.
- ID\_AA64ISAR1\_EL1.API.

For more information, see Pointer authentication.

## FEAT\_PACQARMA3, Pointer authentication - QARMA3 algorithm

FEAT\_PACQARMA3 introduces the QARMA3 cryptographic algorithm for PAC calculation.

This feature is supported in AArch64 state only.

FEAT\_PACQARMA3 is OPTIONAL from Armv8.2.

If FEAT\_PACQARMA3 is implemented, then FEAT\_PAuth is implemented.

If FEAT\_PACQARMA3 is implemented, then FEAT\_PACQARMA5 is not implemented.

If FEAT\_PACQARMA3 is implemented, then FEAT\_PACIMP is not implemented.

The following fields identify the presence of FEAT\_PACQARMA3:

- ID\_AA64ISAR2\_EL1.GPA3.
- ID\_AA64ISAR2\_EL1.APA3.

For more information, see Pointer authentication.

## FEAT\_PACQARMA5, Pointer authentication - QARMA5 algorithm

FEAT\_PACQARMA5 introduces the QARMA5 cryptographic algorithm for PAC calculation.

This feature is supported in AArch64 state only.

FEAT\_PACQARMA5 is OPTIONAL from Armv8.2.

If FEAT\_PACQARMA5 is implemented, then FEAT\_PAuth is implemented.

If FEAT\_PACQARMA5 is implemented, then FEAT\_PACQARMA3 is not implemented.

If FEAT\_PACQARMA5 is implemented, then FEAT\_PACIMP is not implemented.

The following fields identify the presence of FEAT\_PACQARMA5:

- ID\_AA64ISAR1\_EL1.GPA.
- ID\_AA64ISAR1\_EL1.APA.

For more information, see Pointer authentication.

## FEAT\_PAuth, Pointer authentication

FEAT\_PAuth introduces functionality that supports address authentication of the contents of a register before that register is used as the target of an indirect branch, or as a load.

When FEAT\_PAuth is implemented, all of the following must be true:

- Exactly one of the PAC algorithms is implemented.
- The PACGA instruction and other Pointer authentication instructions use the same algorithm.

The PAC algorithm features are:

- FEAT\_PACQARMA5.
- FEAT\_PACIMP.
- FEAT\_PACQARMA3.

This feature is supported in AArch64 state only.

FEAT\_PAuth is OPTIONAL from Armv8.2.

FEAT\_PAuth is mandatory from Armv8.3.

If FEAT\_PAuth is implemented, then FEAT\_PACQARMA5, FEAT\_PACIMP, or FEAT\_PACQARMA3 is implemented.

For more information, see Pointer authentication.

## FEAT\_SPEv1p1, Statistical Profiling Extension version 1.1

FEAT\_SPEv1p1 introduces an Alignment Flag in the Events packet and filtering on this event using PMSEVFR\_EL1, together with support for the profiling of Scalable Vector Extension operations.

This feature is supported in AArch64 state only.

FEAT\_SPEv1p1 is OPTIONAL from Armv8.2.

In an Armv8.5 implementation, if FEAT\_SPE is implemented, FEAT\_SPEv1p1 is implemented.

If FEAT\_SPEv1p1 is implemented, then FEAT\_SPE is implemented.

The following field identifies the presence of FEAT\_SPEv1p1:

- ID\_AA64DFR0\_EL1.PMSVer.

An implementation that includes FEAT\_SVE and the Statistical Profiling Extension is strongly recommended to implement FEAT\_SPEv1p1 whenever possible.

For more information, see:

- The Statistical Profiling Extension.
- Statistical Profiling Extension Sample Record Specification.

## A2.2.5 The Armv8.4 architecture extension

The Armv8.4 architecture extension is an extension to Armv8.3. It adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv8.4 compliant if all of the following apply:

- It is Armv8.3 compliant.
- It includes all of the Armv8.4 architectural features that are mandatory.

An Armv8.4 compliant implementation can additionally include:

- Armv8.4 features that are optional.
- Any arbitrary subset of the architectural features of Armv8.5, subject only to those constraints that require that certain features be implemented together.

## FEAT\_AMU\_EXT, External Activity Monitors

FEAT\_AMU\_EXT indicates support for external access to the Activity Monitors.

FEAT\_AMU\_EXT is OPTIONAL.

If FEAT\_AMU\_EXT is implemented, then FEAT\_AMU\_EXT32 or FEAT\_AMU\_EXT64 is implemented.

If FEAT\_AMU\_EXT is implemented, then FEAT\_AMUv1 is implemented.

## FEAT\_AMU\_EXT32, AArch32 External Activity Monitors

FEAT\_AMU\_EXT32 indicates the external AMU registers are implemented as mostly 32-bit registers.

FEAT\_AMU\_EXT32 is OPTIONAL.

If FEAT\_AMU\_EXT32 is implemented, then FEAT\_AMU\_EXT is implemented.

If FEAT\_AMU\_EXT32 is implemented, then FEAT\_AMU\_EXT64 is not implemented.

The following field identifies the presence of FEAT\_AMU\_EXT32:

- AMDEVARCH.ARCHID.

For more information, see Recommended External Interface to the Activity Monitors.

## FEAT\_AMUv1, Activity Monitors Extension version 1

FEAT\_AMUv1 provides a function similar to a subset of the existing Performance Monitors Extension functionality, intended for system management use rather than debugging and profiling.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_AMUv1 is OPTIONAL from Armv8.3.

The following fields identify the presence of FEAT\_AMUv1:

- ID\_AA64PFR0\_EL1.AMU.
- ID\_PFR0\_EL1.AMU.
- ID\_PFR0.AMU.
- EDPFR.AMU.

For more information, see The Activity Monitors Extension.

## FEAT\_BBML1, Translation table break-before-make level 1

FEAT\_BBML1 provides support for reducing the requirements for following a break-before-make sequence when changing between table or block sizes for a translation.

This feature is supported in AArch64 state only.

FEAT\_BBML1 is OPTIONAL from Armv8.3.

The following field identifies the presence of FEAT\_BBML1:

- ID\_AA64MMFR2\_EL1.BBM.

For more information, see:

- Block descriptor and Page descriptor formats.
- 'Block translation entry'.
- Support levels for changing block size.

## FEAT\_BBML2, Translation table break-before-make level 2

FEAT\_BBML2 provides support for further reducing the requirements for following a break-before-make sequences when changing between table or block sizes for a translation.

This feature is supported in AArch64 state only.

FEAT\_BBML2 is OPTIONAL from Armv8.3.

If FEAT\_BBML2 is implemented, then FEAT\_BBML1 is implemented.

The following field identifies the presence of FEAT\_BBML2:

- ID\_AA64MMFR2\_EL1.BBM.

For more information, see FEAT\_BBML1.

## FEAT\_CNTSC, Generic Counter Scaling

FEAT\_CNTSC introduces a scaling register to the memory-mapped counter module that allows the frequency of the counter that is generated to be scaled from the basic frequency reported in the counter ID mechanisms.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_CNTSC is OPTIONAL from Armv8.3.

The following field identifies the presence of FEAT\_CNTSC:

- CNTID.CNTSC.

For more information, see CNTCR.

## FEAT\_DIT, Data Independent Timing instructions

FEAT\_DIT provides a mechanism for software to indicate that a sequence of code is intended to be independent from data values from certain instructions within the sequence.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_DIT is OPTIONAL from Armv8.3.

FEAT\_DIT is mandatory from Armv8.4.

The following fields identify the presence of FEAT\_DIT:

- ID\_AA64PFR0\_EL1.DIT.
- ID\_PFR0\_EL1.DIT.
- ID\_PFR0.DIT.

For more information, see:

- About PSTATE.DIT.
- About the DIT bit.

## FEAT\_Debugv8p4, Debug v8.4

FEAT\_Debugv8p4 provides the following mandatory changes:

- The fields MDCR\_EL3.{EPMAD, EDAD} control Non-secure access to the debug and PMU registers. The bus Requester is responsible for other debug authentication.
- The Software Lock is obsolete.
- Non-invasive Debug controls are relaxed.
- Secure and Non-secure views of the debug registers are enabled.

FEAT\_Debugv8p4 is OPTIONAL from Armv8.3.

FEAT\_Debugv8p4 is mandatory from Armv8.4.

If FEAT\_Debugv8p4 is implemented, then FEAT\_Debugv8p2 is implemented.

If FEAT\_SEL2 is implemented, then FEAT\_Debugv8p4 is implemented.

The following fields identify the presence of FEAT\_Debugv8p4:

- ID\_DFR0\_EL1.CopDbg.
- ID\_AA64DFR0\_EL1.DebugVer.
- DBGDIDR.Version.
- ID\_DFR0.CopDbg.
- EDDEVARCH.ARCHVER.

For more information, see:

- Definition and constraints of a debugger in the context of external debug.
- External debug interface register access permissions.

## FEAT\_DotProd, Advanced SIMD dot product instructions

FEAT\_DotProd provides instructions to perform a four-way vector dot product of 8-bit integers, accumulating each sum of four products into a 32-bit integer. Each 8-bit input can be treated as a signed or unsigned value.

These instructions are added to the A64 and A32/T32 instruction sets.

FEAT\_DotProd is OPTIONAL from Armv8.1.

In an Armv8.4 implementation, if FEAT\_AdvSIMD is implemented, FEAT\_DotProd is implemented.

The following fields identify the presence of FEAT\_DotProd:

- ID\_AA64ISAR0\_EL1.DP.
- ID\_ISAR6\_EL1.DP.
- ID\_ISAR6.DP.

For more information, see:

- SIMD integer dot product.
- Advanced SIMD dot product instructions.

## FEAT\_DoubleFault, Double Fault Extension

FEAT\_DoubleFault provides controls for routing and masking error exceptions.

This feature is supported in AArch64 state only.

FEAT\_DoubleFault is OPTIONAL from Armv8.3.

In an Armv8.4 implementation, if FEAT\_AA64EL3 is implemented, FEAT\_DoubleFault is implemented.

If FEAT\_DoubleFault is implemented, then FEAT\_DoubleFault2 or FEAT\_AA64EL3 is implemented.

The following field identifies the presence of FEAT\_DoubleFault:

- ID\_AA64PFR0\_EL1.RAS.

For more information, see:

- Taking error exceptions.
- Error synchronization event.

## FEAT\_FHM, Floating-point half-precision to single-precision multiply-add instructions

FEAT\_FHM introduces half-precision to single-precision fused multiply-add instructions.

These instructions are added to the A64 and A32/T32 instruction sets.

FEAT\_FHM is OPTIONAL from Armv8.1.

In an Armv8.4 implementation, if FEAT\_FP16 is implemented, FEAT\_FHM is implemented.

In an Armv8.2 implementation, if FEAT\_FHM is implemented, FEAT\_FP16 is implemented.

The following fields identify the presence of FEAT\_FHM:

- ID\_AA64ISAR0\_EL1.FHM.
- ID\_ISAR6\_EL1.FHM.
- ID\_ISAR6.FHM.

For more information, see:

- SIMD arithmetic.
- SIMD by element arithmetic.
- Advanced SIMD multiply instructions.

## FEAT\_FlagM, Condition flag manipulation instructions

FEAT\_FlagM provides instructions that manipulate the PSTATE.{N,Z,C,V} flags.

These instructions are added to the A64 instruction set only.

FEAT\_FlagM is OPTIONAL from Armv8.1.

FEAT\_FlagM is mandatory from Armv8.4.

The following field identifies the presence of FEAT\_FlagM:

- ID\_AA64ISAR0\_EL1.TS.

For more information, see Flag manipulation instructions.

## FEAT\_IDST, ID space trap handling

FEAT\_IDST causes all AArch64 read accesses to the feature ID space when exceptions are generated to be reported in ESR\_ELx using the EC code 0x18 .

This feature is supported in AArch64 state only.

FEAT\_IDST is OPTIONAL from Armv8.3.

FEAT\_IDST is mandatory from Armv8.4.

The following field identifies the presence of FEAT\_IDST:

- ID\_AA64MMFR2\_EL1.IDS.

## FEAT\_LRCPC2, Load-Acquire RCpc instructions version 2

FEAT\_LRCPC2 provides versions of LDAPR and STLR with a 9-bit unscaled signed immediate offset.

These instructions are added to the A64 instruction set only.

FEAT\_LRCPC2 is OPTIONAL from Armv8.2.

FEAT\_LRCPC2 is mandatory from Armv8.4.

If FEAT\_LRCPC2 is implemented, then FEAT\_LRCPC is implemented.

The following field identifies the presence of FEAT\_LRCPC2:

- ID\_AA64ISAR1\_EL1.LRCPC.

For more information, see:

- Changes to single-copy atomicity in Armv8.4.
- Load-Acquire/Store-Release.
- A64 instructions that are changed in Debug state.

## FEAT\_LSE2, Large System Extensions version 2

FEAT\_LSE2 introduces changes to single-copy atomicity requirements for loads and stores, and changes to alignment requirements for loads and stores.

This feature is supported in AArch64 state only.

FEAT\_LSE2 is OPTIONAL from Armv8.2.

FEAT\_LSE2 is mandatory from Armv8.4.

The following field identifies the presence of FEAT\_LSE2:

- ID\_AA64MMFR2\_EL1.AT.

For more information, see:

- Requirements for single-copy atomicity.
- Alignment of data accesses.

## FEAT\_MPAM, Memory System Resource Partitioning and Monitoring Extension

The MPAM Extension provides a framework for memory-system component controls that partition one or more of the performance resources of the component. There are three versions of the MPAM extension: v1p0, v1p1, and v0p1.

This feature is supported in AArch64 state only.

FEAT\_MPAM is OPTIONAL from Armv8.2.

If FEAT\_MPAM is implemented, then FEAT\_MPAMv1p0 or FEAT\_MPAMv0p1 is implemented.

For more information, see MPAM PE Architecture.

## FEAT\_MPAMv1p0, Memory Partitioning and Monitoring Extension version 1.0

FEAT\_MPAMv1p0 introduces support for version 1.0 of the MPAM extension.

This feature is supported in AArch64 state only.

FEAT\_MPAMv1p0 is OPTIONAL from Armv8.2.

If FEAT\_MPAMv1p0 is implemented, then FEAT\_MPAM is implemented.

If FEAT\_MPAMv1p0 is implemented, then FEAT\_MPAMv0p1 is not implemented.

The following field identifies the presence of FEAT\_MPAMv1p0:

- ID\_AA64PFR0\_EL1.MPAM.

For more information, see MPAM PE Architecture.

## FEAT\_NV2, Enhanced nested virtualization support

FEAT\_NV2 supports nested virtualization by redirecting register accesses that would be trapped to EL1 and EL2 to access memory instead. The address of the memory access depends on information held in VNCR\_EL2.

This feature is supported in AArch64 state only.

FEAT\_NV2 is OPTIONAL from Armv8.3.

If FEAT\_NV2 is implemented, then FEAT\_NV is implemented.

The following fields identify the presence of FEAT\_NV2:

- ID\_AA64MMFR4\_EL1.NV\_frac.
- ID\_AA64MMFR2\_EL1.NV.

For more information, see Enhanced support for nested virtualization.

## FEAT\_PMUv3p4, Arm8.4 PMU extensions

FEAT\_PMUv3p4 introduces:

- PMMIR\_EL1
- PMMIRregisters.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_PMUv3p4 is OPTIONAL from Armv8.3.

In an Armv8.4 implementation, if FEAT\_PMUv3 is implemented, FEAT\_PMUv3p4 is implemented.

If FEAT\_PMUv3p4 is implemented, then FEAT\_PMUv3p1 is implemented.

The following fields identify the presence of FEAT\_PMUv3p4:

- ID\_AA64DFR0\_EL1.PMUVer.
- ID\_DFR0\_EL1.PerfMon.

- ID\_DFR0.PerfMon.
- EDDFR.PMUVer.

For more information, see PMU Event Descriptions.

## FEAT\_RASSAv1p1, RAS version 1.1 System Architecture

FEAT\_RASSAv1p1 implements the RAS System Architecture v1.1, including support for the following:

- Additional ERR&lt;n&gt;MISC&lt;m&gt; registers.
- The optional RAS Common Fault Injection Model Extension.

FEAT\_RASSAv1p1 is OPTIONAL from Armv8.2.

In an Armv8.4 implementation, if FEAT\_RAS is implemented, FEAT\_RASSAv1p1 is implemented.

If FEAT\_RASv1p1 is implemented, then FEAT\_RASSAv1p1 is implemented.

## FEAT\_RASv1p1, RAS extension v1.1

FEAT\_RASv1p1 introduces support for System register access to the following RAS System Architecture v1.1 features:

- Additional ERR&lt;n&gt;MISC&lt;m&gt; registers.
- The optional RAS Common Fault Injection Model Extension.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_RASv1p1 is OPTIONAL from Armv8.2.

In an Armv8.4 implementation, if FEAT\_RAS is implemented, FEAT\_RASv1p1 is implemented.

If FEAT\_RASv1p1 is implemented, then FEAT\_RAS is implemented.

If FEAT\_RASv1p1 is implemented, then FEAT\_RASSAv1p1 is implemented.

The following fields identify the presence of FEAT\_RASv1p1:

- ID\_AA64PFR0\_EL1.RAS.
- ID\_AA64PFR1\_EL1.RAS\_frac.
- ID\_PFR0\_EL1.RAS.
- ID\_PFR2\_EL1.RAS\_frac.
- ID\_PFR0.RAS.
- ID\_PFR2.RAS\_frac.

For more information, see Arm ® Reliability Availability and Serviceability (RAS) System Architecture, for A-profile architecture (ARM IHI 0100).

## FEAT\_S2FWB, Stage 2 forced Write-Back

FEAT\_S2FWB reduces the requirement of additional cache maintenance instructions in systems where the data Cacheability attributes used by the Guest operating system are different from those expected by the Hypervisor. If this feature is implemented, there is no meaningful distinction between the Inner and Outer Shareability domains for accesses to Normal Cacheable memory.

This feature is supported in AArch64 state only.

FEAT\_S2FWB is OPTIONAL from Armv8.3.

In an Armv8.4 implementation, if FEAT\_EL2 is implemented, FEAT\_S2FWB is implemented.

The following field identifies the presence of FEAT\_S2FWB:

- ID\_AA64MMFR2\_EL1.FWB.

For more information, see:

- Block descriptor and Page descriptor formats.
- Stage 2 memory type and Cacheability attributes when FEAT\_S2FWB is enabled.

## FEAT\_SEL2, Secure EL2

FEAT\_SEL2 permits EL2 to be implemented in Secure state. When Secure EL2 is enabled, a translation regime is introduced that follows the same format as the other Secure translation regimes.

This feature is not supported if EL2 is using AArch32.

FEAT\_SEL2 is OPTIONAL from Armv8.3.

In an Armv8.4 implementation, if FEAT\_AA64EL2 and FEAT\_Secure are implemented, FEAT\_SEL2 is implemented.

If FEAT\_SEL2 is implemented, then FEAT\_TTST is implemented.

If FEAT\_SEL2 is implemented, then FEAT\_PCSRv8 is not implemented.

If FEAT\_SEL2 is implemented, then FEAT\_EL2 is implemented.

If FEAT\_SEL2 is implemented, then FEAT\_Secure is implemented.

The following field identifies the presence of FEAT\_SEL2:

- ID\_AA64PFR0\_EL1.SEL2.

For more information, see:

- Security states
- Translation regimes.

## FEAT\_TLBIOS, TLB invalidate instructions in Outer Shareable domain

FEAT\_TLBIOS provides TLBI maintenance instructions that extend to the Outer Shareable domain.

This feature is supported in AArch64 state only.

FEAT\_TLBIOS is OPTIONAL from Armv8.3.

FEAT\_TLBIOS is mandatory from Armv8.4.

The following field identifies the presence of FEAT\_TLBIOS:

- ID\_AA64ISAR0\_EL1.TLB.

For more information, see TLB maintenance instructions.

## FEAT\_TLBIRANGE, TLB invalidate range instructions

FEAT\_TLBIRANGE provides TLBI maintenance instructions that apply to a range of input addresses.

This feature is supported in AArch64 state only.

FEAT\_TLBIRANGE is OPTIONAL from Armv8.3.

FEAT\_TLBIRANGE is mandatory from Armv8.4.

If FEAT\_TLBIRANGE is implemented, then FEAT\_TLBIOS is implemented.

The following field identifies the presence of FEAT\_TLBIRANGE:

- ID\_AA64ISAR0\_EL1.TLB.

For more information, see:

- TLB maintenance instructions.
- TLB maintenance instructions that do not apply to a range of addresses.

## FEAT\_TRF, Self-hosted Trace extensions

FEAT\_TRF introduces control of trace in a self-hosted system through System registers.

The feature provides:

- Control of Exception levels and Security states where trace generation is prohibited.
- Control of whether an offset is used for the timestamp recorded with trace information.
- Acontext synchronization instruction, TSB CSYNC, that can be used to prevent reordering of trace operation accesses with respect to other accesses of the same System registers.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_TRF is OPTIONAL from Armv8.3.

In an Armv8.4 implementation, if FEAT\_ETMv4 is implemented, FEAT\_TRF is implemented.

If FEAT\_TRF is implemented, then FEAT\_TRC\_SR is implemented.

The following fields identify the presence of FEAT\_TRF:

- ID\_DFR0\_EL1.TraceFilt.
- ID\_AA64DFR0\_EL1.TraceFilt.
- ID\_DFR0.TraceFilt.
- EDDFR.TraceFilt.

For more information on FEAT\_TRF, see:

- AArch64 Self-hosted Trace.
- AArch32 Self-hosted Trace.

## FEAT\_TTL, Translation Table Level

FEAT\_TTL provides the TTL field to indicate the level of translation table walk holding the leaf entry for the address that is being invalidated. This field is provided in all TLB maintenance instructions that take a V A or an IPA argument.

This feature is supported in AArch64 state only.

FEAT\_TTL is OPTIONAL from Armv8.3.

FEAT\_TTL is mandatory from Armv8.4.

The following field identifies the presence of FEAT\_TTL:

- ID\_AA64MMFR2\_EL1.TTL.

For more information, see:

- TLB maintenance instructions.
- TLB maintenance instructions that do not apply to a range of addresses.

## FEAT\_TTST, Small translation tables

FEAT\_TTST relaxes the lower limit on the size of translation tables, by increasing the maximum permitted value of the T1SZ and T0SZ fields in TCR\_EL1, TCR\_EL2, TCR\_EL3, VTCR\_EL2 and VSTCR\_EL2.

This feature is supported in AArch64 state only.

FEAT\_TTST is OPTIONAL from Armv8.3.

If FEAT\_SEL2 is implemented, then FEAT\_TTST is implemented.

The following field identifies the presence of FEAT\_TTST:

- ID\_AA64MMFR2\_EL1.ST.

For more information, see:

- Input address size configuration.
- Translation using the 4KB granule.
- Translation using the 16KB granule.
- Translation using the 64KB granule.

## A2.2.5.1 Features added to the Armv8.4 extension in later releases

- FEAT\_AMU\_EXTACR.
- FEAT\_NV2p1.

## A2.2.6 The Armv8.5 architecture extension

The Armv8.5 architecture extension is an extension to Armv8.4. It adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv8.5 compliant if all of the following apply:

- It is Armv8.4 compliant.
- It includes all of the Armv8.5 architectural features that are mandatory.

An Armv8.5 compliant implementation can additionally include:

- Armv8.5 features that are optional.
- Any arbitrary subset of the architectural features of Armv8.6, subject only to those constraints that require that certain features be implemented together.

## FEAT\_BTI, Branch Target Identification

FEAT\_BTI allows memory pages to be guarded against the execution of instructions that are not the intended target of a branch. To do this, it introduces:

- The GP field, which denotes the blocks and pages in stage 1 translation tables that are guarded pages.
- The PSTATE.BTYPE field, which is used to determine whether an access to a guarded memory region will generate a Branch Target exception.
- The BTI instruction, which is used to guard against the execution of instructions that are not the intended target of a branch.

This feature is supported in AArch64 state only.

FEAT\_BTI is OPTIONAL from Armv8.4.

FEAT\_BTI is mandatory from Armv8.5.

The following field identifies the presence of FEAT\_BTI:

- ID\_AA64PFR1\_EL1.BT.

For more information, see:

- Table descriptor format.
- PSTATE.BTYPE.
- Effect of entering Debug state on PSTATE.

## FEAT\_CSV3, Cache Speculation Variant 3

FEAT\_CSV3 introduces a mechanism to identify whether data loaded or read from a register under speculation where the data load or register read would not be permitted architecturally, can be used by instructions newer than the load or register read in a manner that allows the value of the inaccessible data to be recovered by code architecturally executed.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_CSV3 is OPTIONAL from Armv8.0.

FEAT\_CSV3 is mandatory from Armv8.5.

The following field identifies the presence of FEAT\_CSV3:

- ID\_AA64PFR0\_EL1.CSV3.

## FEAT\_DPB2, DC CVADP instruction

FEAT\_DPB2 allows two levels of cache clean to the Point of Persistence by:

- Redefining Point of Persistence, which changes the scope of DC CV AP.
- Defining a Point of Deep Persistence.
- Adding the DC CVADP System instruction.

This feature is supported in AArch64 state only.

FEAT\_DPB2 is OPTIONAL from Armv8.1.

FEAT\_DPB2 is mandatory from Armv8.5.

If FEAT\_DPB2 is implemented, then FEAT\_DPB is implemented.

The following field identifies the presence of FEAT\_DPB2:

- ID\_AA64ISAR1\_EL1.DPB.

For more information, see Terminology for Clean, Invalidate, and Clean and Invalidate instructions.

## FEAT\_E0PD, Preventing EL0 access to halves of address maps

FEAT\_E0PD prevents access at EL0 to half of the addresses in the memory map.

This feature is supported in AArch64 state only. When EL1 is using AArch64 state, this feature affects access to EL0, in either Execution state.

FEAT\_E0PD is OPTIONAL from Armv8.4.

FEAT\_E0PD is mandatory from Armv8.5.

If FEAT\_E0PD is implemented, then FEAT\_CSV3 is implemented.

The following field identifies the presence of FEAT\_E0PD:

- ID\_AA64MMFR2\_EL1.E0PD.

For more information, see Preventing EL0 access to halves of the address map.

## FEAT\_EVT, Enhanced Virtualization Traps

FEAT\_EVT introduces additional traps for EL1 and EL0 Cache controls in:

- HCR\_EL2
- HCR2.

These traps are independent of existing controls.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_EVT is OPTIONAL from Armv8.2.

In an Armv8.5 implementation, if FEAT\_EL2 is implemented, FEAT\_EVT is implemented.

The following fields identify the presence of FEAT\_EVT:

- ID\_AA64MMFR2\_EL1.EVT.
- ID\_MMFR4\_EL1.EVT.
- ID\_MMFR4.EVT.

## FEAT\_ExS, Context synchronization and exception handling

FEAT\_ExS provides a mechanism to control whether exception entry and exception return are Context Synchronization events.

Fields in the SCTLR\_ELx registers enable and disable context synchronization at exception entry and return at an Exception level.

This feature is supported in AArch64 state only.

FEAT\_ExS is OPTIONAL from Armv8.4.

The following field identifies the presence of FEAT\_ExS:

- ID\_AA64MMFR0\_EL1.ExS.

For more information, see 'Context Synchronization event'.

## FEAT\_FRINTTS, Floating-point to integer instructions

FEAT\_FRINTTS provides instructions that round a floating-point number to an integral valued floating-point number that fits in a 32-bit or 64-bit integer number range.

These instructions are added to the A64 instruction set only.

FEAT\_FRINTTS is OPTIONAL from Armv8.4.

In an Armv8.5 implementation, if FEAT\_FP is implemented, FEAT\_FRINTTS is implemented.

If FEAT\_FRINTTS is implemented, then FEAT\_FP and FEAT\_AdvSIMD are implemented.

The following field identifies the presence of FEAT\_FRINTTS:

- ID\_AA64ISAR1\_EL1.FRINTTS.

For more information, see Floating-point round to integral value.

## FEAT\_FlagM2, Enhancements to flag manipulation instructions

FEAT\_FlagM2 provides instructions that convert between the PSTATE condition flag format used by the FCMP instruction and an alternative format described in Condition flags and related instructions.

These instructions are added to the A64 instruction set only.

FEAT\_FlagM2 is OPTIONAL from Armv8.4.

If FEAT\_FlagM2 is implemented, then FEAT\_FlagM is implemented.

The following field identifies the presence of FEAT\_FlagM2:

- ID\_AA64ISAR0\_EL1.TS.

For more information, see Flag manipulation instructions.

## FEAT\_GTG, Guest translation granule size

FEAT\_GTG allows a hypervisor to support different granule sizes for stage 2 and stage 1 translation, and allows a nested hypervisor to determine what stage 2 granule sizes are available.

This feature is supported in AArch64 state only.

FEAT\_GTG is OPTIONAL from Armv8.0.

In an Armv8.5 implementation, if FEAT\_AA64EL2 is implemented, FEAT\_GTG is implemented.

The following fields identify the presence of FEAT\_GTG:

- ID\_AA64MMFR0\_EL1.TGran4\_2.
- ID\_AA64MMFR0\_EL1.TGran16\_2.
- ID\_AA64MMFR0\_EL1.TGran64\_2.

For more information, see Translation granules.

## FEAT\_MTE, Memory Tagging Extension

FEAT\_MTE provides architectural support for runtime, always-on detection of various classes of memory error to aid with software debugging to eliminate vulnerabilities arising from memory-unsafe languages.

These features are supported in AArch64 state only.

FEAT\_MTE is OPTIONAL from Armv8.4.

The following field identifies the presence of FEAT\_MTE:

- ID\_AA64PFR1\_EL1.MTE.

For more information, see:

- The Memory Tagging Extension.
- The AArch64 Application Level Memory Model.
- PMUEvent Descriptions.
- The Statistical Profiling Extension.
- Debug State.

## FEAT\_MTE2, Memory Tagging Extension

FEAT\_MTE2 provides architectural support for runtime, always-on detection of various classes of memory error to aid with software debugging to eliminate vulnerabilities arising from memory-unsafe languages.

These features are supported in AArch64 state only.

FEAT\_MTE2 is OPTIONAL from Armv8.4.

If FEAT\_MTE2 is implemented, then FEAT\_MTE is implemented.

The following field identifies the presence of FEAT\_MTE2:

- ID\_AA64PFR1\_EL1.MTE.

For more information, see:

- The Memory Tagging Extension.
- The AArch64 Application Level Memory Model.
- PMUEvent Descriptions.
- The Statistical Profiling Extension.
- Debug State.

## FEAT\_PMUv3p5, Arm8.5 PMU extensions

FEAT\_PMUv3p5 extends event counters to 64-bit event counters, and introduces mechanisms to disable the cycle counter in Secure state, in EL3, and in EL2.

FEAT\_PMUv3p5 relaxes the behavior of PMCR.{IMP, IDCODE}, and deprecates use of these fields.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_PMUv3p5 is OPTIONAL from Armv8.4.

In an Armv8.5 implementation, if FEAT\_PMUv3 is implemented, FEAT\_PMUv3p5 is implemented.

If FEAT\_PMUv3p5 is implemented, then FEAT\_PMUv3p4 is implemented.

The following fields identify the presence of FEAT\_PMUv3p5:

- ID\_AA64DFR0\_EL1.PMUVer.
- ID\_DFR0\_EL1.PerfMon.
- ID\_DFR0.PerfMon.
- EDDFR.PMUVer.

For more information, see:

- Behavior on overflow.
- Controlling the PMU counters.
- PMUEvent Descriptions.

## FEAT\_RNG, Random number generator

FEAT\_RNG introduces the RNDR and RNDRRS registers. Reads to these registers return a 64-bit random number. A read to RNDRRS will cause a reseeding of the random number before the generation of the random number that is returned.

This feature is supported in AArch64 state only.

FEAT\_RNG is OPTIONAL from Armv8.4.

The following field identifies the presence of FEAT\_RNG:

- ID\_AA64ISAR0\_EL1.RNDR.

For more information, see:

- Effect of random number generation instructions on Condition flags
- Appendix K14 Random Number Generation

## FEAT\_RNG\_TRAP, Trapping support for RNDR/RNDRRS

FEAT\_RNG\_TRAP introduces support for EL3 trapping of reads of the RNDR and RNDRRS registers.

This feature is supported in AArch64 state only.

FEAT\_RNG\_TRAP is OPTIONAL from Armv8.4.

The following field identifies the presence of FEAT\_RNG\_TRAP:

- ID\_AA64PFR1\_EL1.RNDR\_trap.

## FEAT\_S2TGran16K, Support for 16KB memory translation granule size at stage 2

FEAT\_S2TGran16K is OPTIONAL.

If FEAT\_S2TGran16K is implemented, then FEAT\_AA64EL2 and FEAT\_TGran16K are implemented.

The following field identifies the presence of FEAT\_S2TGran16K:

- ID\_AA64MMFR0\_EL1.TGran16\_2.

## FEAT\_S2TGran4K, Support for 4KB memory translation granule size at stage 2

FEAT\_S2TGran4K is OPTIONAL.

If FEAT\_S2TGran4K is implemented, then FEAT\_AA64EL2 and FEAT\_TGran4K are implemented.

The following field identifies the presence of FEAT\_S2TGran4K:

- ID\_AA64MMFR0\_EL1.TGran4\_2.

## FEAT\_S2TGran64K, Support for 64KB memory translation granule size at stage 2

FEAT\_S2TGran64K is OPTIONAL.

If FEAT\_S2TGran64K is implemented, then FEAT\_AA64EL2 and FEAT\_TGran64K are implemented.

The following field identifies the presence of FEAT\_S2TGran64K:

- ID\_AA64MMFR0\_EL1.TGran64\_2.

## FEAT\_SB, Speculation Barrier

Speculation Barrier FEAT\_SB introduces a barrier to control speculation.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_SB is OPTIONAL from Armv8.0.

FEAT\_SB is mandatory from Armv8.5.

The following fields identify the presence of FEAT\_SB:

- ID\_AA64ISAR1\_EL1.SB.
- ID\_ISAR6\_EL1.SB.
- ID\_ISAR6.SB.

For more information, see:

- Speculation Barrier (SB).
- Barriers and CLREX instructions.
- Speculation Barrier (SB).
- Miscellaneous instructions.

## FEAT\_SPECRES, Speculation restriction instructions

FEAT\_SPECRES introduces System instructions that prevent predictions based on information gathered from earlier execution within a particular execution context from affecting the later speculative execution within that context, to the extent that the speculative execution is observable through side channels.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_SPECRES is OPTIONAL from Armv8.0.

FEAT\_SPECRES is mandatory from Armv8.5.

The following fields identify the presence of FEAT\_SPECRES:

- ID\_AA64ISAR1\_EL1.SPECRES.
- ID\_ISAR6\_EL1.SPECRES.
- ID\_ISAR6.SPECRES.

For more information, see:

- Prediction restriction instructions.
- Execution, data prediction and prefetching restriction System instructions.
- Execution and data prediction restriction System instructions.

## FEAT\_SSBS, Speculative Store Bypass Safe

FEAT\_SSBS allows software to indicate whether hardware is permitted to load or store speculatively in a manner that could give rise to a cache timing side channel, which in turn could be used to derive an address from values loaded to a register from memory.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_SSBS is OPTIONAL from Armv8.0.

The following fields identify the presence of FEAT\_SSBS:

- ID\_AA64PFR1\_EL1.SSBS.
- ID\_PFR2\_EL1.SSBS.
- ID\_PFR2.SSBS.

For more information, see:

- AArch64 Speculative Store Bypass Safe.
- AArch32 Speculative Store Bypass Safe.

## FEAT\_SSBS2, MRS and MSR instructions for SSBS version 2

FEAT\_SSBS2 provides controls for the MSR and MRS instructions to read and write the PSTATE.SSBS field.

This feature is supported in AArch64 state only.

FEAT\_SSBS2 is OPTIONAL from Armv8.0.

If FEAT\_SSBS2 is implemented, then FEAT\_SSBS is implemented.

The following field identifies the presence of FEAT\_SSBS2:

- ID\_AA64PFR1\_EL1.SSBS.

For more information, see:

- AArch64 Speculative Store Bypass Safe.
- AArch32 Speculative Store Bypass Safe.

## A2.2.6.1 Features added to the Armv8.5 extension in later releases

- FEAT\_MTE3.
- FEAT\_MTE\_ASYNC.

## A2.2.7 The Armv8.6 architecture extension

The Armv8.6 architecture extension is an extension to Armv8.5. It adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv8.6 compliant if all of the following apply:

- It is Armv8.5 compliant.
- It includes all of the Armv8.6 architectural features that are mandatory.

An Armv8.6 compliant implementation can additionally include:

- Armv8.6 features that are optional.
- Any arbitrary subset of the architectural features of Armv8.7, subject only to those constraints that require that certain features be implemented together.

## FEAT\_AA32BF16, AArch32 BFloat16 instructions

FEAT\_AA32BF16 supports the BFloat16, or BF16, 16-bit floating-point storage format in AArch32 state. This format supports:

- Arithmetic instructions to multiply BFloat16 values and accumulate into single-precision results.
- Arithmetic instructions to accelerate dot product and matrix multiply-accumulate of BFloat16 values into single-precision results.
- Instructions to convert single-precision floating-point values to BFloat16 format.

This feature is supported in AArch32 state only.

FEAT\_AA32BF16 is OPTIONAL from Armv8.2.

If FEAT\_AA32BF16 is implemented, then FEAT\_BF16 is implemented.

If FEAT\_AA32BF16 is implemented, then FEAT\_AA32 is implemented.

The following fields identify the presence of FEAT\_AA32BF16:

- ID\_ISAR6\_EL1.BF16.
- ID\_ISAR6.BF16.

For more information, see:

- BFloat16 floating-point format.
- Advanced SIMD BFloat16 instructions.
- Floating-point data-processing.

## FEAT\_AMUv1p1, Activity Monitors Extension version 1.1

FEAT\_AMUv1p1 introduces support for virtualization of Activity Monitors event counters, and introduces controls to disable access to auxiliary event counters below the highest Exception level.

This feature is supported in AArch32 state and AArch64 state, if the hypervisor is using AArch64.

FEAT\_AMUv1p1 is OPTIONAL from Armv8.5.

If FEAT\_AMUv1p1 is implemented, then FEAT\_AMUv1 is implemented.

The following fields identify the presence of FEAT\_AMUv1p1:

- ID\_AA64PFR0\_EL1.AMU.
- ID\_PFR0\_EL1.AMU.
- ID\_PFR0.AMU.
- EDPFR.AMU.

For more information, see The Activity Monitors Extension.

## FEAT\_BF16, AArch64 BFloat16 instructions

FEAT\_BF16 supports the BFloat16, or BF16, 16-bit floating-point storage format in AArch64 state. This format supports:

- Arithmetic instructions to multiply BFloat16 values and accumulate into single-precision results.
- Arithmetic instructions to accelerate dot product and matrix multiply-accumulate of BFloat16 values into single-precision results.
- Instructions to convert single-precision floating-point values to BFloat16 format.

This feature is supported in AArch64 state only.

FEAT\_BF16 is OPTIONAL from Armv8.2.

In an Armv8.6 implementation, if FEAT\_FP is implemented, FEAT\_BF16 is implemented.

The following fields identify the presence of FEAT\_BF16:

- ID\_AA64ISAR1\_EL1.BF16.
- ID\_AA64ZFR0\_EL1.BF16.

For more information, see:

- BFloat16 floating-point format.
- Summary of BFloat16 instruction behaviors.

## FEAT\_CP15SDISABLE2, CP15SDISABLE2

FEAT\_CP15SDISABLE2 provides an implementation-defined mechanism, the CP15SDISABLE2 signal, which when asserted HIGH prevents writes to a set of Secure CP15 registers. This signal is analogous to the existing CP15SDISABLE signal.

This feature is supported only when EL3 is executing in AArch32 state.

FEAT\_CP15SDISABLE2 is OPTIONAL from Armv8.0.

When FEAT\_AA32 and FEAT\_CP15SDISABLE2 are implemented, FEAT\_AA32EL3 is implemented.

For more information, see The CP15SDISABLE and CP15SDISABLE2 input signals.

## FEAT\_DGH, Data Gathering Hint

FEAT\_DGH introduces the Data Gathering Hint instruction to the hint space.

This instruction is added to the A64 instruction set only.

FEAT\_DGH is OPTIONAL from Armv8.0.

The following field identifies the presence of FEAT\_DGH:

- ID\_AA64ISAR1\_EL1.DGH.

For more information, see Hint instructions.

## FEAT\_ECV, Enhanced Counter Virtualization

FEAT\_ECV enhances the Generic Timer architecture. FEAT\_ECV provides:

- Self-synchronizing views of the virtual and physical timers in AArch64 state and AArch32 state.
- The ability to scale the generation of the event stream when executing in AArch64 state or AArch32 state.
- When EL2 is using AArch64 state, traps to EL0 and EL1 access to the virtual counter or timer registers, and the physical timer registers when accessed using an EL02 mnemonic. The traps are configured in CNTHCTL\_EL2, and apply to EL1 and EL0 accesses, whether EL1 and EL0 are in AArch64 state or AArch32 state.

For more information on the offset to views of physical time, see FEAT\_ECV\_POFF.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_ECV is OPTIONAL from Armv8.5.

FEAT\_ECV is mandatory from Armv8.6.

The following field identifies the presence of FEAT\_ECV:

- ID\_AA64MMFR0\_EL1.ECV.

For more information, see:

- Self-hosted trace timestamps.
- The profiling data.
- The AArch64 view of the Generic Timer.
- The AArch32 view of the Generic Timer.

## FEAT\_ECV\_POFF, Enhanced Counter Virtualization Physical Offset

FEAT\_ECV\_POFF provides an offset between the EL1 or EL0 view of physical time, and the EL2 or EL3 view of physical time.

The offset to views of physical time at EL1 and EL0 apply in AArch64 state and AArch32 state.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_ECV\_POFF is OPTIONAL from Armv8.5.

If FEAT\_ECV\_POFF is implemented, then FEAT\_ECV is implemented.

When FEAT\_AA64 and FEAT\_ECV\_POFF are implemented, FEAT\_AA64EL2 is implemented.

If FEAT\_RME is implemented, then FEAT\_ECV\_POFF is implemented.

The following field identifies the presence of FEAT\_ECV\_POFF:

- ID\_AA64MMFR0\_EL1.ECV.

## FEAT\_FGT, Fine Grain Traps

FEAT\_FGT introduces additional traps to EL2 of EL1 and EL0 access to individual or small groups of System registers and instructions, and traps to EL3 and EL2 of the Debug Communications Channel registers. The traps are independent of existing controls.

This feature is supported in AArch64, and when EL1 is using AArch64, EL0 accesses using AArch32 are also trapped.

FEAT\_FGT is OPTIONAL from Armv8.5.

In an Armv8.6 implementation, if FEAT\_AA64EL2 or FEAT\_AA64EL3 is implemented, FEAT\_FGT is implemented.

The following field identifies the presence of FEAT\_FGT:

- ID\_AA64MMFR0\_EL1.FGT.

For more information, see Configurable instruction controls.

## FEAT\_HPMN0, Setting of MDCR\_EL2.HPMN to zero

FEAT\_HPMN0 permits a hypervisor to provide zero PMU event counters for a guest operating system by setting MDCR\_EL2.HPMN to zero.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_HPMN0 is OPTIONAL from Armv8.5.

In an Armv8.8 implementation, if FEAT\_PMUv3 and FEAT\_EL2 are implemented, FEAT\_HPMN0 is implemented.

If FEAT\_HPMN0 is implemented, then FEAT\_EL2 is implemented.

If FEAT\_HPMN0 is implemented, then FEAT\_PMUv3 and FEAT\_FGT are implemented.

The following fields identify the presence of FEAT\_HPMN0:

- ID\_AA64DFR0\_EL1.HPMN0.
- ID\_DFR1\_EL1.HPMN0.
- ID\_DFR1.HPMN0.

For more information, see:

- Interaction with EL2.
- Controlling the PMU counters.
- The Performance Monitors Extension.
- The Performance Monitors Extension.

## FEAT\_MPAMv0p1, Memory System Resource Partitioning and Monitoring extension version 0.1

FEAT\_MPAMv0p1 introduces support for version 0.1 of the MPAM extension.

This feature is supported in AArch64 state only.

FEAT\_MPAMv0p1 is OPTIONAL from Armv8.5.

If FEAT\_MPAMv0p1 is implemented, then FEAT\_MPAM is implemented.

The following fields identify the presence of FEAT\_MPAMv0p1:

- ID\_AA64PFR0\_EL1.MPAM.
- ID\_AA64PFR1\_EL1.MPAM\_frac.

For more information, see MPAM PE Architecture.

## FEAT\_MPAMv1p1, Memory Partitioning and Monitoring extension version 1.1

FEAT\_MPAMv1p1 introduces support for version 1.1 of the MPAM extension.

This feature is supported in AArch64 state only.

FEAT\_MPAMv1p1 is OPTIONAL from Armv8.5.

If FEAT\_MPAMv1p1 is implemented, then FEAT\_MPAM is implemented.

If FEAT\_MPAMv1p1 is implemented, then FEAT\_MPAMv0p1 is not implemented.

The following fields identify the presence of FEAT\_MPAMv1p1:

- ID\_AA64PFR0\_EL1.MPAM.
- ID\_AA64PFR1\_EL1.MPAM\_frac.

For more information, see MPAM PE Architecture.

## FEAT\_MTPMU, Multi-threaded PMU extensions

FEAT\_MTPMU introduces controls to disable PMEVTYPER&lt;n&gt;\_EL0.MT.

From Armv8.6, when FEAT\_PMUv3 is implemented, multithreaded event counting is only supported in multithreaded implementations that also include FEAT\_MTPMU.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_MTPMU is OPTIONAL from Armv8.5.

If FEAT\_MTPMU is implemented, then FEAT\_PMUv3 is implemented.

If FEAT\_MTPMU is implemented, then FEAT\_EL2 or FEAT\_EL3 is implemented.

The following fields identify the presence of FEAT\_MTPMU:

- ID\_AA64DFR0\_EL1.MTPMU.
- ID\_DFR1.MTPMU.
- ID\_DFR1\_EL1.MTPMU.

For more information, see:

- Multithreaded implementations.
- MDCR\_EL3.MTPME
- SDCR.MTPME
- MDCR\_EL2.MTPME
- HDCR.MTPME.

## FEAT\_PAuth2, Enhancements to pointer authentication

FEAT\_PAuth2 introduces enhanced pointer authentication functionality that changes the mechanism by which a PAC is added to the pointer.

This feature is supported in AArch64 state only.

FEAT\_PAuth2 is OPTIONAL from Armv8.2.

FEAT\_PAuth2 is mandatory from Armv8.6.

If FEAT\_PAuth2 is implemented, then FEAT\_PAuth is implemented.

If FEAT\_PAuth2 is implemented, then FEAT\_EPAC is not implemented.

The following fields identify the presence of FEAT\_PAuth2:

- ID\_AA64ISAR1\_EL1.APA.
- ID\_AA64ISAR1\_EL1.API.
- ID\_AA64ISAR2\_EL1.APA3.

For more information, see Pointer authentication.

## FEAT\_TWED, Delayed Trapping of WFE

FEAT\_TWED introduces support for configurable delayed trapping of the WFE and WFET instructions.

FEAT\_TWED is OPTIONAL from Armv8.5.

The following field identifies the presence of FEAT\_TWED:

- ID\_AA64MMFR1\_EL1.TWED.

For more information, see The Wait for Event and Wait for Event with Timeout instructions.

## A2.2.7.1 Features added to the Armv8.6 extension in later releases

- FEAT\_SPE\_DPFZS.

## A2.2.8 The Armv8.7 architecture extension

The Armv8.7 architecture extension is an extension to Armv8.6. It adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv8.7 compliant if all of the following apply:

- It is Armv8.6 compliant.
- It includes all of the Armv8.7 architectural features that are mandatory.

An Armv8.7 compliant implementation can additionally include:

- Armv8.7 features that are optional.
- Any arbitrary subset of the architectural features of Armv8.8, subject only to those constraints that require that certain features be implemented together.

## FEAT\_AFP, Alternate floating-point behavior

FEAT\_AFP allows alternate behavior for specified floating-point instructions including:

- Flushing of denormalized numbers to zero can be controlled separately on inputs and outputs.
- Alternate NaN propagation rules and Default NaN values can apply.
- Certain scalar SIMD and floating-point instructions can be configured to preserve higher numbered SIMD vector elements.
- Changes to floating-point exception generation.

This feature is supported in AArch64 state only.

FEAT\_AFP is OPTIONAL from Armv8.6.

In an Armv8.7 implementation, if FEAT\_FP is implemented, FEAT\_AFP is implemented.

If FEAT\_AFP is implemented, then FEAT\_FP is implemented.

The following field identifies the presence of FEAT\_AFP:

- ID\_AA64MMFR1\_EL1.AFP.

For more information, see:

- Flushing denormalized numbers to zero.
- NaN handling and the Default NaN.
- Rounding.
- Floating-point exceptions and exception traps.

## FEAT\_EBF16, AArch64 Extended BFloat16 behaviors

FEAT\_EBF16 supports the Extended BFloat16 behaviors.

This feature is supported in AArch64 state only.

FEAT\_EBF16 is OPTIONAL from Armv8.2.

If FEAT\_EBF16 is implemented, then FEAT\_BF16 is implemented.

If FEAT\_EBF16 is implemented, then FEAT\_AdvSIMD, FEAT\_FP, FEAT\_SVE, or FEAT\_SME is implemented.

The following fields identify the presence of FEAT\_EBF16:

- ID\_AA64ISAR1\_EL1.BF16.
- ID\_AA64ZFR0\_EL1.BF16.

For more information, see:

- BFloat16 floating-point format.
- Floating-point behaviors for instructions that compute sum-of-products.

## FEAT\_HCX, Support for the HCRX\_EL2 register

FEAT\_HCX introduces the Extended Hypervisor Configuration Register, HCRX\_EL2, that provides configuration controls for virtualization in addition to those provided by HCR\_EL2, including defining whether various operations are trapped to EL2.

This feature is supported in AArch64 state only.

FEAT\_HCX is OPTIONAL from Armv8.6.

In an Armv8.7 implementation, if FEAT\_AA64EL2 is implemented, FEAT\_HCX is implemented.

When FEAT\_AA64 and FEAT\_HCX are implemented, FEAT\_AA64EL2 is implemented.

The following field identifies the presence of FEAT\_HCX:

- ID\_AA64MMFR1\_EL1.HCX.

For more information, see Configurable instruction controls.

## FEAT\_LPA2, Larger physical address for 4KB and 16KB translation granules

FEAT\_LPA2:

- Allows a larger V A space for each translation table base register of up to 52 bits when using the 4KB or 16KB translation granules.
- Allows a larger intermediate physical address (IPA) and PA space of up to 52 bits when using the 4KB or 16KB translation granules.
- Allows a level 0 block size where the block covers a 512GB address range for the 4KB translation granule if the implementation supports 52 bits of PA.
- Allows a level 1 block size where the block covers a 64GB address range for the 16KB translation granule if the implementation supports 52 bits of PA.

This feature is supported in AArch64 state only.

FEAT\_LPA2 is OPTIONAL from Armv8.6.

If FEAT\_LPA2 is implemented, then FEAT\_LVA is implemented.

The following fields identify the presence of FEAT\_LPA2:

- ID\_AA64MMFR0\_EL1.TGran4\_2.
- ID\_AA64MMFR0\_EL1.TGran16\_2.
- ID\_AA64MMFR0\_EL1.TGran4.
- ID\_AA64MMFR0\_EL1.TGran16.

For more information, see:

- Implemented physical address size.
- Output address size configuration.
- Supported virtual address ranges.
- Input address size configuration.
- Intermediate physical address size configuration.
- Translation using the 4KB granule.
- Translation using the 16KB granule.
- Table descriptor format.
- Block descriptor and Page descriptor formats.

## FEAT\_LS64, Support for 64-byte loads and stores without status

FEAT\_LS64 introduces support for single-copy atomic 64-byte loads and stores without status result. For more information, see:

- LD64B.
- ST64B.

This feature is supported in AArch64 state only.

FEAT\_LS64 is OPTIONAL from Armv8.6.

The following field identifies the presence of FEAT\_LS64:

- ID\_AA64ISAR1\_EL1.LS64.

For more information, see Single-copy atomic 64-byte load/store.

## FEAT\_LS64\_ACCDATA, Support for 64-byte EL0 stores with status

FEAT\_LS64\_ACCDATA introduces support for single-copy atomic 64-byte EL0 stores with status result. For more information, see:

- ST64BV0.
- ACCDATA\_EL1.

Note

The meaning of any status being returned by the ST64BV0 instruction is defined by the peripheral providing the response.

This feature is supported in AArch64 state only.

FEAT\_LS64\_ACCDATA is OPTIONAL from Armv8.6.

If FEAT\_LS64\_ACCDATA is implemented, then FEAT\_LS64\_V is implemented.

The following field identifies the presence of FEAT\_LS64\_ACCDATA:

- ID\_AA64ISAR1\_EL1.LS64.

For more information, see Single-copy atomic 64-byte load/store.

## FEAT\_LS64\_V, Support for 64-byte stores with status

FEAT\_LS64\_V introduces support for single-copy atomic 64-byte stores with status result. For more information, see:

- ST64BV.

Note

The meaning of any status being returned by the ST64BV instruction is defined by the peripheral providing the response.

This feature is supported in AArch64 state only.

FEAT\_LS64\_V is OPTIONAL from Armv8.6.

If FEAT\_LS64\_V is implemented, then FEAT\_LS64 is implemented.

The following field identifies the presence of FEAT\_LS64\_V:

- ID\_AA64ISAR1\_EL1.LS64.

For more information, see Single-copy atomic 64-byte load/store.

## FEAT\_MTE3, MTE Asymmetric Fault Handling

FEAT\_MTE3 introduces support for asymmetric Tag Check Fault handling.

This feature is supported in AArch64 state only.

FEAT\_MTE3 is OPTIONAL from Armv8.5.

In an Armv8.7 implementation, if FEAT\_MTE\_ASYNC is implemented, FEAT\_MTE3 is implemented.

If FEAT\_MTE3 is implemented, then FEAT\_MTE2 is implemented.

The following field identifies the presence of FEAT\_MTE3:

- ID\_AA64PFR1\_EL1.MTE.

For more information, see The Memory Tagging Extension.

## FEAT\_MTE\_ASYM\_FAULT, Memory tagging asymmetric faults

FEAT\_MTE\_ASYM\_FAULT introduces support for asymmetric MTE Tag Check fault handling.

This feature is supported in AArch64 state only.

FEAT\_MTE\_ASYM\_FAULT is OPTIONAL.

If FEAT\_MTE3 is implemented, then FEAT\_MTE\_ASYM\_FAULT is implemented.

If FEAT\_MTE\_ASYM\_FAULT is implemented, then FEAT\_MTE3 is implemented.

If FEAT\_MTE\_ASYM\_FAULT is implemented, then FEAT\_MTE\_ASYNC is implemented.

The following field identifies the presence of FEAT\_MTE\_ASYM\_FAULT:

- ID\_AA64PFR1\_EL1.MTE.

## FEAT\_PAN3, Support for SCTLR\_ELx.EPAN

FEAT\_PAN3 introduces a bit to SCTLR\_EL1 and SCTLR\_EL2, EPAN, to support using Privileged Access Never with instruction accesses for stage 1 translation regimes.

This feature is supported in AArch64 state only.

FEAT\_PAN3 is OPTIONAL from Armv8.1.

FEAT\_PAN3 is mandatory from Armv8.7.

If FEAT\_PAN3 is implemented, then FEAT\_PAN2 is implemented.

The following field identifies the presence of FEAT\_PAN3:

- ID\_AA64MMFR1\_EL1.PAN.

For more information, see PSTATE PAN.

## FEAT\_PMUv3p7, Armv8.7 PMU extensions

FEAT\_PMUv3p7 introduces the following to the Performance Monitors Extension:

- PMUcounters can be frozen when an event counter has an unsigned overflow.
- Event counters can be prohibited from counting events at EL3 without affecting other Exception levels in Secure state.
- The cycle counter can be prohibited from counting cycles at EL3 without affecting other Exception levels in Secure state.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_PMUv3p7 is OPTIONAL from Armv8.6.

In an Armv8.7 implementation, if FEAT\_PMUv3 is implemented, FEAT\_PMUv3p7 is implemented.

If FEAT\_PMUv3p7 is implemented, then FEAT\_PMUv3p5 is implemented.

The following fields identify the presence of FEAT\_PMUv3p7:

- ID\_AA64DFR0\_EL1.PMUVer.
- ID\_DFR0\_EL1.PerfMon.
- ID\_DFR0.PerfMon.
- EDDFR.PMUVer.
- PMCFGR.FZO.

For more information, see:

- Controlling the PMU counters.
- Freezing event counters.

## FEAT\_RPRES, Increased precision of FRECPE and FRSQRTE

FEAT\_RPRES allows an increase in the precision of the single-precision floating-point reciprocal estimate and reciprocal square root estimate from an 8-bit mantissa to a 12-bit mantissa.

This feature is supported in AArch64 state only.

FEAT\_RPRES is OPTIONAL from Armv8.6.

If FEAT\_RPRES is implemented, then FEAT\_AFP is implemented.

The following field identifies the presence of FEAT\_RPRES:

- ID\_AA64ISAR2\_EL1.RPRES.

For more information, see RecipEstimate() and RecipSqrtEstimate() .

## FEAT\_SPE\_FnE, Statistical Profiling inverse event filter

FEAT\_SPE\_FnE provides the capability to filter sample records by the inverse value of bits in the sampled Events packet.

This feature is supported in AArch64 state only.

FEAT\_SPE\_FnE is OPTIONAL.

If FEAT\_SPE\_FnE is implemented, then FEAT\_SPEv1p2 is implemented.

If FEAT\_SPEv1p2 is implemented, then FEAT\_SPE\_FnE is implemented.

The following field identifies the presence of FEAT\_SPE\_FnE:

- PMSIDR\_EL1.FnE.

For more information, see Filtering sample records.

## FEAT\_SPE\_PBT, Statistical Profiling previous branch target

FEAT\_SPE\_PBT provides support for generating a packet that provides the target address for the previous taken branch.

This feature is supported in AArch64 state only.

FEAT\_SPE\_PBT is OPTIONAL.

If FEAT\_SPE\_PBT is implemented, then FEAT\_SPEv1p2 is implemented.

The following field identifies the presence of FEAT\_SPE\_PBT:

- PMSIDR\_EL1.PBT.

For more information, see:

- Previous branch target.
- Address packet.

## FEAT\_SPEv1p2, Statistical Profiling Extensions version 1.2

FEAT\_SPEv1p2 introduces the following to the Statistical Profiling Extension:

- Controls to freeze the PMU event counters after an SPE buffer management event occurs.
- Adiscard mode that allows all SPE data to be discarded rather than written to memory.

This feature is supported in AArch64 state only.

FEAT\_SPEv1p2 is OPTIONAL from Armv8.6.

In an Armv8.7 implementation, if FEAT\_SPE is implemented, FEAT\_SPEv1p2 is implemented.

If FEAT\_SPEv1p2 is implemented, then FEAT\_SPEv1p1 is implemented.

The following field identifies the presence of FEAT\_SPEv1p2:

- ID\_AA64DFR0\_EL1.PMSVer.

For more information, see:

- Freezing event counters.
- Discard mode.

## FEAT\_WFxT, WFE and WFI instructions with timeout

FEAT\_WFxT introduces WFET and WFIT. These instructions support the generation of a local timeout event to act as a wake-up event for the PE when the virtual count in CNTVCT\_EL0 equals or exceeds the value supplied by the instruction for the first time.

These instructions are added to the A64 instruction set only.

FEAT\_WFxT is OPTIONAL from Armv8.6.

FEAT\_WFxT is mandatory from Armv8.7.

The following field identifies the presence of FEAT\_WFxT:

- ID\_AA64ISAR2\_EL1.WFxT.

For more information, see:

- Wait for Event.
- Wait for Interrupt mechanism.

## FEAT\_XS, XS attribute

FEAT\_XS introduces the XS attribute for memory to indicate that an access could take a long time to complete. This feature provides variants of DSB instructions and TLB maintenance instructions, the completion of which does not depend on the completion of memory accesses with the XS attribute.

FEAT\_XS adds:

- Amechanism to define the XS attribute for memory.
- An optional nXS variant to the AArch64 DSB instruction and OPTIONAL nXS qualifier to each AArch64 TLBI instruction to handle memory accesses with the XS attribute.
- The HCRX\_EL2.FGTnXS bit to determine the behavior of fine-grained traps in HFGITR\_EL2 for TLB maintenance instructions with the nXS qualifier.
- The HCRX\_EL2.FnXS bit to determine the behavior of pre-existing TLB maintenance instructions in relation to the XS attribute.

This feature is supported in AArch64 state only, but the XS attribute also impacts AArch32 state execution.

FEAT\_XS is OPTIONAL from Armv8.6.

FEAT\_XS is mandatory from Armv8.7.

The following field identifies the presence of FEAT\_XS:

- ID\_AA64ISAR1\_EL1.XS.

For more information, see:

- Data Synchronization Barrier (DSB).
- Behavior when stage 1 address translation is disabled.
- Block descriptor and Page descriptor formats.

- Stage 1 memory type and Cacheability attributes.
- XS attribute modifier.
- Overview of memory region attributes for stage 1 translations.
- Ordering and completion of TLB maintenance instructions.

## A2.2.8.1 Features added to the Armv8.7 extension in later releases

- FEAT\_CSSC.
- FEAT\_HAFT.
- FEAT\_MTE4.
- FEAT\_MTE\_PERM.

## A2.2.9 The Armv8.8 architecture extension

The Armv8.8 architecture extension is an extension to Armv8.7. It adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv8.8 compliant if all of the following apply:

- It is Armv8.7 compliant.
- It includes all of the Armv8.8 architectural features that are mandatory.

An Armv8.8 compliant implementation can additionally include:

- Armv8.8 features that are optional.
- Any arbitrary subset of the architectural features of Armv8.9, subject only to those constraints that require that certain features be implemented together.

## FEAT\_CMOW, Control for cache maintenance permission

FEAT\_CMOWintroduces support for controlling the required permissions for some cache maintenance instructions that operate by VA and perform translation such that:

- Stage 1 can be configured to generate a Permission fault if write permission is not present for cache maintenance instructions executed at EL0.
- Stage 2 can be configured to generate a Permission fault if write permission is not present for cache maintenance instructions executed at EL1 or EL0.

This feature is supported in AArch64 state only, but also impacts AArch32 instructions.

FEAT\_CMOWisOPTIONAL from Armv8.7.

FEAT\_CMOWis mandatory from Armv8.8.

The following field identifies the presence of FEAT\_CMOW:

- ID\_AA64MMFR1\_EL1.CMOW.

For more information, see:

- A64 Cache maintenance instructions.
- Permission fault.

## FEAT\_Debugv8p8, Debug v8.8

FEAT\_Debugv8p8 introduces support to allow an asynchronous exception to be taken after an exception generates an Exception Catch debug event, but before the PE halts.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_Debugv8p8 is OPTIONAL from Armv8.7.

FEAT\_Debugv8p8 is mandatory from Armv8.8.

If FEAT\_Debugv8p8 is implemented, then FEAT\_Debugv8p4 is implemented.

The following fields identify the presence of FEAT\_Debugv8p8:

- ID\_AA64DFR0\_EL1.DebugVer.
- ID\_DFR0\_EL1.CopDbg.
- DBGDIDR.Version.
- ID\_DFR0.CopDbg.
- EDDEVARCH.ARCHVER.

For more information, see Exception Catch debug event.

## FEAT\_HBC, Hinted conditional branches

FEAT\_HBC provides the BC.cond instruction to give a conditional branch to a label at a PC-relative offset, with a hint that this branch is very unlikely to change direction.

This feature is supported in AArch64 state only.

FEAT\_HBC is OPTIONAL from Armv8.7.

FEAT\_HBC is mandatory from Armv8.8.

The following field identifies the presence of FEAT\_HBC:

- ID\_AA64ISAR2\_EL1.BC.

For more information, see Conditional branch.

## FEAT\_MOPS, Standardization of memory operations

FEAT\_MOPS provides instructions that perform a memory copy or memory set, and introduces Memory Copy and Memory Set exceptions.

FEAT\_MOPS also introduces the HCRX\_EL2.{MSCEn, MCE2}, SCTLR\_EL1.MSCEn, and SCTLR\_EL2.MSCEn control bits.

This feature is supported in AArch64 state only.

FEAT\_MOPS is OPTIONAL from Armv8.7.

FEAT\_MOPS is mandatory from Armv8.8.

The following field identifies the presence of FEAT\_MOPS:

- ID\_AA64ISAR2\_EL1.MOPS.

For more information, see:

- Memory Copy and Memory Set instructions.
- Memory Copy and Memory Set exceptions.

## FEAT\_NMI, Non-maskable Interrupts

FEAT\_NMI provides a mechanism to support non-maskable interrupts (NMI) and less-masked interrupts (LMI). In addition to legacy behavior, the feature includes the following:

- Amode for supporting an LMI interrupt mask that is distinct from PSTATE.{I, F}.
- Amode for supporting a limited NMI, where the value when PSTATE.SP is 1 is taken as an interrupt mask for all interrupts targeting that Exception level, and where the LMI interrupt mask can also be used

FEAT\_NMI adds:

- The AllIntMask variable.
- An Optional Superpriority attribute to denote virtual and physical IRQ and FIQ interrupts as non-maskable.
- The SCTLR\_ELx.{NMI, SPINTMASK} control bits.
- The PSTATE.ALLINT bit and associated instructions.
- The HCRX\_EL2.TALLINT bit to enable trapping of ALLINT instructions at EL1.

This feature is supported in AArch64 state only.

FEAT\_NMI is OPTIONAL from Armv8.7.

FEAT\_NMI is mandatory from Armv8.8.

The following field identifies the presence of FEAT\_NMI:

- ID\_AA64PFR1\_EL1.NMI.

For more information, see:

- Asynchronous exception types.
- Virtual interrupts.
- PSTATE fields that are meaningful in AArch64 state.
- WFEwake-up events.

## FEAT\_PMUv3\_EXT64, 64-bit external interface to the Performance Monitors

FEAT\_PMUv3\_EXT64 indicates the external Performance Monitors registers are implemented as 64-bit registers. The 32-bit CoreSight management registers remain 32-bit registers.

FEAT\_PMUv3\_EXT64 is OPTIONAL from Armv8.8.

If FEAT\_PMUv3\_EXT64 is implemented, then FEAT\_PMUv3\_EXT is implemented.

If FEAT\_PMUv3\_EXT64 is implemented, then FEAT\_PMUv3\_EXT32 is not implemented.

The following field identifies the presence of FEAT\_PMUv3\_EXT64:

- PMDEVARCH.ARCHPART.

For more information, see Recommended External Interface to the Performance Monitors.

## FEAT\_PMUv3\_TH, Event counting threshold

FEAT\_PMUv3\_TH introduces threshold condition controls to each PMEVTYPER&lt;n&gt;\_EL0 register. This feature permits the counter to count only when PMEVTYPER&lt;n&gt;.{MT, evtCount} describe an event whose count meets a specified threshold condition.

This feature is supported in both AArch64 and AArch32 states. The threshold condition controls are accessible only in AArch64 state. However, threshold conditions still apply in AArch32 state.

FEAT\_PMUv3\_TH is OPTIONAL from Armv8.7.

If FEAT\_PMUv3\_TH is implemented, then FEAT\_PMUv3 is implemented.

The following fields identify the presence of FEAT\_PMUv3\_TH:

- PMMIR\_EL1.THWIDTH.
- PMMIR.THWIDTH.
- PMMIR.THWIDTH.

For more information, see Event threshold and edge counting.

## FEAT\_PMUv3p8, Armv8.8 PMU extensions

FEAT\_PMUv3p8 introduces the following to the Performance Monitors Extension:

- The Common event number space is extended to include the ranges 0x0040 -0x00BF and 0x4040 -0x40BF .
- For an event counter n, if any reserved or unimplemented PMU event number is written to PMEVTYPER&lt;n&gt;.evtCount, then event counter n does not count, and a read of PMEVTYPER&lt;n&gt;.evtCount returns the value written.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_PMUv3p8 is OPTIONAL from Armv8.7.

In an Armv8.8 implementation, if FEAT\_PMUv3 is implemented, FEAT\_PMUv3p8 is implemented.

If FEAT\_PMUv3p8 is implemented, then FEAT\_PMUv3p7 is implemented.

The following fields identify the presence of FEAT\_PMUv3p8:

- ID\_AA64DFR0\_EL1.PMUVer.
- ID\_DFR0\_EL1.PerfMon.
- ID\_DFR0.PerfMon.
- EDDFR.PMUVer.

For more information, see PMU Event Descriptions.

## FEAT\_SCTLR2, Extension to SCTLR\_ELx

FEAT\_SCTLR2 introduces the SCTLR2\_ELx registers, which provide top-level control of the system, including its memory system. These registers are extensions of the corresponding SCTLR\_ELx registers.

This feature is supported in AArch64 state only.

FEAT\_SCTLR2 is OPTIONAL from Armv8.0.

FEAT\_SCTLR2 is mandatory from Armv8.9.

When FEAT\_SCTLR2 and FEAT\_AA64EL2 are implemented, FEAT\_HCX is implemented.

The following field identifies the presence of FEAT\_SCTLR2:

- ID\_AA64MMFR3\_EL1.SCTLRX.

## FEAT\_SPEv1p3, Statistical Profiling Extensions version 1.3

FEAT\_SPEv1p3 introduces the following to the Statistical Profiling Extension:

- Support for sampling Tag operations.
- Support for sampling Memory Copy and Set operations.

This feature is supported in AArch64 state only.

FEAT\_SPEv1p3 is OPTIONAL from Armv8.7.

In an Armv8.8 implementation, if FEAT\_SPE is implemented, FEAT\_SPEv1p3 is implemented.

If FEAT\_SPEv1p3 is implemented, then FEAT\_SPEv1p2 is implemented.

The following field identifies the presence of FEAT\_SPEv1p3:

- ID\_AA64DFR0\_EL1.PMSVer.

For more information, see:

- Additional information for each profiled memory access operation.
- About the Statistical Profiling Extension sample records.
- Address packet.

## FEAT\_TCR2, Support for TCR2\_ELx

FEAT\_TCR2 introduces the TCR2\_ELx registers which provide top-level control of the EL1&amp;0 and EL2&amp;0 translation regimes respectively. These registers are extensions of the corresponding TCR\_ELx registers.

This feature is supported in AArch64 state only.

FEAT\_TCR2 is OPTIONAL from Armv8.0.

FEAT\_TCR2 is mandatory from Armv8.9.

When FEAT\_TCR2 and FEAT\_AA64EL2 are implemented, FEAT\_HCX is implemented.

The following field identifies the presence of FEAT\_TCR2:

- ID\_AA64MMFR3\_EL1.TCRX.

## FEAT\_TIDCP1, EL0 use of IMPLEMENTATION DEFINED functionality

FEAT\_TIDCP1 introduces a control at EL1 and EL2 to enable trapping of EL0 accesses to registers that might control IMPLEMENTATION DEFINED functions.

This feature introduces controls only in AArch64 state, and controls IMPLEMENTATION DEFINED execution at EL0 in both AArch32 and AArch64 states.

FEAT\_TIDCP1 is OPTIONAL from Armv8.7.

FEAT\_TIDCP1 is mandatory from Armv8.8.

The following field identifies the presence of FEAT\_TIDCP1:

- ID\_AA64MMFR1\_EL1.TIDCP1.

For more information, see Prioritization of Synchronous exceptions taken to AArch64 state

## A2.2.10 The Armv8.9 architecture extension

The Armv8.9 architecture extension is an extension to Armv8.8. It adds mandatory and optional architectural features. Some features must be implemented together. An implementation is Armv8.9 compliant if all of the following apply:

- It is Armv8.8 compliant.
- It includes all of the Armv8.9 architectural features that are mandatory.

An Armv8.9 compliant implementation can additionally include:

- Armv8.9 features that are optional.

## FEAT\_ADERR, Asynchronous Device Error Exceptions

FEAT\_ADERR introduces controls for whether an error signaled on a load from Device memory is handled precisely and synchronously.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_ADERR is OPTIONAL from Armv8.8.

If FEAT\_ADERR is implemented, then FEAT\_RASv2 is implemented.

If FEAT\_ADERR is implemented, then FEAT\_SCTLR2 is implemented.

When FEAT\_AA64 and FEAT\_ADERR are implemented, FEAT\_AA64EL1 is implemented.

When FEAT\_ADERR and FEAT\_AA64EL2 are implemented, FEAT\_HCX is implemented.

The following fields identify the presence of FEAT\_ADERR:

- ID\_AA64MMFR3\_EL1.ADERR.
- ID\_AA64MMFR3\_EL1.SDERR.

For more information, see:

- About the RAS Extension.
- Taking error exceptions.

## FEAT\_AIE, Memory Attribute Index Enhancement

FEAT\_AIE increases the stage 1 descriptor attribute index bit width from 3 to 4, allowing use of up to 16 memory attributes.

This feature is supported in AArch64 state only.

FEAT\_AIE is OPTIONAL from Armv8.8.

If FEAT\_AIE is implemented, then FEAT\_TCR2 is implemented.

If FEAT\_AIE is implemented, then FEAT\_HPDS is implemented.

The following field identifies the presence of FEAT\_AIE:

- ID\_AA64MMFR3\_EL1.AIE.

For more information, see Stage 1 memory type and Cacheability attributes.

## FEAT\_AMU\_EXT64, the 64-bit external Activity Monitors extension

FEAT\_AMU\_EXT64 indicates the external AMU registers are implemented as 64-bit registers.

FEAT\_AMU\_EXT64 is OPTIONAL.

If FEAT\_AMU\_EXT64 is implemented, then FEAT\_AMU\_EXT is implemented.

If FEAT\_AMU\_EXT64 is implemented, then FEAT\_AMU\_EXT32 is not implemented.

The following field identifies the presence of FEAT\_AMU\_EXT64:

- AMDEVARCH.ARCHID.

For more information, see Recommended External Interface to the Activity Monitors.

## FEAT\_ANERR, Asynchronous Normal Error Exceptions

FEAT\_ANERR introduces controls for whether an error signaled on a load from Normal memory is handled precisely and synchronously.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_ANERR is OPTIONAL from Armv8.8.

If FEAT\_ANERR is implemented, then FEAT\_RASv2 is implemented.

If FEAT\_ANERR is implemented, then FEAT\_SCTLR2 is implemented.

When FEAT\_AA64 and FEAT\_ANERR are implemented, FEAT\_AA64EL1 is implemented.

When FEAT\_ANERR and FEAT\_AA64EL2 are implemented, FEAT\_HCX is implemented.

The following fields identify the presence of FEAT\_ANERR:

- ID\_AA64MMFR3\_EL1.ANERR.
- ID\_AA64MMFR3\_EL1.SNERR.

For more information, see:

- About the RAS Extension.
- Taking error exceptions.

## FEAT\_ATS1A, Address Translation operations that ignore stage 1 permissions

FEAT\_ATS1A introduces instructions that provide the output address and attributes of a valid translation without checking for stage 1 permissions.

These instructions are added to the A64 instruction set only.

FEAT\_ATS1A is OPTIONAL from Armv8.8.

The following field identifies the presence of FEAT\_ATS1A:

- ID\_AA64ISAR2\_EL1.ATS1A.

## FEAT\_CLRBHB, Support for Clear Branch History instruction

FEAT\_CLRBHB provides a CLRBHB instruction, which can be used to clear the branch history.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_CLRBHB is OPTIONAL from Armv8.0.

FEAT\_CLRBHB is mandatory from Armv8.9.

The following fields identify the presence of FEAT\_CLRBHB:

- ID\_AA64ISAR2\_EL1.CLRBHB.
- ID\_ISAR6\_EL1.CLRBHB.
- ID\_ISAR6.CLRBHB.

For more information, see:

- Branch prediction.
- AArch32 cache and branch predictor maintenance instructions.

## FEAT\_CSSC, Common Short Sequence Compression instructions

FEAT\_CSSC introduces a set of instructions for optimization of short instruction sequences using general-purpose registers.

This feature is supported in AArch64 state only.

FEAT\_CSSC is OPTIONAL from Armv8.7.

FEAT\_CSSC is mandatory from Armv8.9.

The following field identifies the presence of FEAT\_CSSC:

- ID\_AA64ISAR2\_EL1.CSSC.

For more information, see:

- Integer minimum and maximum (immediate).
- Integer maximum and minimum (register).
- Absolute value.
- Bit operation.

## FEAT\_Debugv8p9, Debug v8.9

FEAT\_Debugv8p9 introduces all of the following:

- The ability to implement more than 16 breakpoints.
- The ability to implement more than 16 watchpoints.
- DBGBCR&lt;n&gt;\_EL1 and DBGWCR&lt;n&gt;\_EL1 are 64-bit registers in the external debug interface.
- DSPSR2 is added to extend DSPSR for holding the saved process state for Debug state.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_Debugv8p9 is OPTIONAL from Armv8.8.

FEAT\_Debugv8p9 is mandatory from Armv8.9.

If FEAT\_Debugv8p9 is implemented, then FEAT\_Debugv8p8 is implemented.

When FEAT\_Debugv8p9 and FEAT\_AA64EL2 are implemented, FEAT\_FGT2 is implemented.

The following fields identify the presence of FEAT\_Debugv8p9:

- ID\_AA64DFR0\_EL1.DebugVer.
- ID\_DFR0\_EL1.CopDbg.
- ID\_DFR0.CopDbg.
- DBGDIDR.Version.
- EDDEVARCH.ARCHVER.
- EDDEVID1.HSR.

For more information, see:

- About Breakpoint exceptions.
- About Watchpoint exceptions.

## FEAT\_DoubleFault2, Double Fault Extension v2

FEAT\_DoubleFault2 provides additional controls for routing and masking error exceptions.

This feature is supported in AArch64 state only.

FEAT\_DoubleFault2 is OPTIONAL from Armv8.8.

If FEAT\_DoubleFault2 is implemented, then FEAT\_SCTLR2 is implemented.

When FEAT\_AA64 and FEAT\_DoubleFault2 are implemented, FEAT\_AA64EL1 is implemented.

When FEAT\_DoubleFault2 and FEAT\_AA64EL2 are implemented, FEAT\_HCX is implemented.

If FEAT\_DoubleFault2 is implemented, then FEAT\_DoubleFault is implemented.

The following field identifies the presence of FEAT\_DoubleFault2:

- ID\_AA64PFR1\_EL1.DF2.

For more information, see:

- Synchronous exception types.
- Asynchronous exception types.
- Error synchronization event.

## FEAT\_ECBHB, Exploitative control using branch history information

FEAT\_ECBHB imposes restrictions on branch history speculation around exceptions.

This feature is supported in AArch64 state only.

FEAT\_ECBHB is OPTIONAL from Armv8.0.

FEAT\_ECBHB is mandatory from Armv8.9.

The following field identifies the presence of FEAT\_ECBHB:

- ID\_AA64MMFR1\_EL1.ECBHB.

For more information, see Branch prediction.

## FEAT\_EDHSR, Support for EDHSR

FEAT\_EDHSR introduces the EDHSR, which holds syndrome information of a Debug event.

FEAT\_EDHSR is OPTIONAL.

If FEAT\_Debugv8p9 is implemented, then FEAT\_EDHSR is implemented.

If FEAT\_EDHSR is implemented, then FEAT\_Debugv8p2 is implemented.

The following field identifies the presence of FEAT\_EDHSR:

- EDDEVID1.HSR.

## FEAT\_FGT2, Fine-grained traps 2

FEAT\_FGT2 introduces the hypervisor registers HFGITR2\_EL2, HFGRTR2\_EL2, HFGWTR\_EL2, HDFGRTR2\_EL2, and HDFGWTR2\_EL2. These registers are extensions of the corresponding FGT registers.

This feature is supported in AArch64, and in AArch32 at EL0 when EL1 is using AArch64.

FEAT\_FGT2 is OPTIONAL from Armv8.8.

In an Armv8.9 implementation, if FEAT\_AA64EL2 is implemented, FEAT\_FGT2 is implemented.

If FEAT\_FGT2 is implemented, then FEAT\_FGT is implemented.

The following field identifies the presence of FEAT\_FGT2:

- ID\_AA64MMFR0\_EL1.FGT.

## FEAT\_HAFT, Hardware managed Access Flag for Table descriptors

FEAT\_HAFT introduces the support for hardware management of the Table descriptor Access flag.

This feature is supported in AArch64 state only.

FEAT\_HAFT is OPTIONAL from Armv8.7.

If FEAT\_HAFT is implemented, then FEAT\_HAFDBS is implemented.

If FEAT\_HAFT is implemented, then FEAT\_TCR2 is implemented.

The following field identifies the presence of FEAT\_HAFT:

- ID\_AA64MMFR1\_EL1.HAFDBS.

For more information, see Hardware management of the Table descriptor Access Flag.

## FEAT\_LRCPC3, Load-Acquire RCpc instructions version 3

FEAT\_LRCPC3 introduces variants of load/store pair and load/store single register instructions, with release consistency, to optimize additional use cases where ordering is required. FEAT\_LRCPC3 also introduces a set of additional load/store instructions with release consistency ordering in the Advanced SIMD and floating-point instruction set.

This feature is supported in AArch64 state only.

FEAT\_LRCPC3 is OPTIONAL from Armv8.2.

If FEAT\_LRCPC3 is implemented, then FEAT\_LRCPC2 is implemented.

The following field identifies the presence of FEAT\_LRCPC3:

- ID\_AA64ISAR1\_EL1.LRCPC.

For more information, see:

- Changes to single-copy atomicity in Armv8.4.
- Load-Acquire/Store-Release.
- A64 instructions that are changed in Debug state.

## FEAT\_MTE4, Enhanced Memory Tagging Extension

FEAT\_MTE4 introduces support for the following sub-features:

- Canonical tag checking, identified as FEAT\_MTE\_CANONICAL\_TAGS.
- Reporting of all non-address bits on a fault, identified as FEAT\_MTE\_TAGGED\_FAR.
- Store-only Tag checking, identified as FEAT\_MTE\_STORE\_ONLY.
- Memory tagging with Address tagging disabled, identified as FEAT\_MTE\_NO\_ADDRESS\_TAGS.

This feature is supported in AArch64 state only.

FEAT\_MTE4 is OPTIONAL from Armv8.7.

In an Armv8.9 implementation, if FEAT\_MTE2 is implemented, FEAT\_MTE4 is implemented.

If FEAT\_MTE4 is implemented, then FEAT\_MTE2 is implemented.

If FEAT\_MTE4 is implemented, then FEAT\_MTE\_PERM is implemented.

If FEAT\_MTE4 is implemented, then FEAT\_MTE\_CANONICAL\_TAGS, FEAT\_MTE\_NO\_ADDRESS\_TAGS, FEAT\_MTE\_TAGGED\_FAR, and FEAT\_MTE\_STORE\_ONLY are implemented.

## FEAT\_MTE\_ASYNC, Asynchronous reporting of Tag Check Fault

FEAT\_MTE\_ASYNC provides support for asynchronously accumulating Tag Check Faults into the TFSRE0\_EL1 or TFSR\_ELx registers. A PE that is compliant with FEAT\_MTE2 is compliant with the behavior defined for this feature.

This feature is supported in AArch64 state only.

FEAT\_MTE\_ASYNC is OPTIONAL from Armv8.5.

If FEAT\_MTE\_ASYNC is implemented, then FEAT\_MTE2 is implemented.

The following field identifies the presence of FEAT\_MTE\_ASYNC:

- ID\_AA64PFR1\_EL1.MTE\_frac.

For more information, see:

- The Memory Tagging Extension.
- The AArch64 Application Level Memory Model.
- PMUEvent Descriptions.
- The Statistical Profiling Extension.
- Debug State.

## FEAT\_MTE\_CANONICAL\_TAGS, Canonical Tag checking for Untagged memory

FEAT\_MTE\_CANONICAL\_TAGS introduces support for MTE canonical tag checking.

This feature is supported in AArch64 state only.

FEAT\_MTE\_CANONICAL\_TAGS is OPTIONAL.

If FEAT\_MTE\_CANONICAL\_TAGS is implemented, then FEAT\_MTE4 is implemented.

The following field identifies the presence of FEAT\_MTE\_CANONICAL\_TAGS:

- ID\_AA64PFR1\_EL1.MTEX.

## FEAT\_MTE\_NO\_ADDRESS\_TAGS, Memory tagging with Address tagging disabled

FEAT\_MTE\_NO\_ADDRESS\_TAG introduces support for MTE tagging with Address tagging disabled.

This feature is supported in AArch64 state only.

FEAT\_MTE\_NO\_ADDRESS\_TAGS is OPTIONAL.

If FEAT\_MTE\_NO\_ADDRESS\_TAGS is implemented, then FEAT\_MTE4 is implemented.

The following field identifies the presence of FEAT\_MTE\_NO\_ADDRESS\_TAGS:

- ID\_AA64PFR1\_EL1.MTEX.

## FEAT\_MTE\_PERM, Allocation tag access permission

FEAT\_MTE\_PERM introduces support for the Stage 2 NoTagAccess memory attribute.

This feature is supported in AArch64 state only.

FEAT\_MTE\_PERM is OPTIONAL from Armv8.7.

In an Armv8.9 implementation, if FEAT\_MTE2 is implemented, FEAT\_MTE\_PERM is implemented.

If FEAT\_MTE\_PERM is implemented, then FEAT\_MTE2 is implemented.

The following field identifies the presence of FEAT\_MTE\_PERM:

- ID\_AA64PFR2\_EL1.MTEPERM.

## FEAT\_MTE\_STORE\_ONLY, Store-only Tag Checking

This feature is supported in AArch64 state only.

FEAT\_MTE\_STORE\_ONLY is OPTIONAL.

If FEAT\_MTE\_STORE\_ONLY is implemented, then FEAT\_MTE4 is implemented.

The following field identifies the presence of FEAT\_MTE\_STORE\_ONLY:

- ID\_AA64PFR2\_EL1.MTESTOREONLY.

## FEAT\_MTE\_TAGGED\_FAR, FAR\_ELx on a Tag Check Fault

FEAT\_MTE\_TAGGED\_FAR introduces support for reporting all non-address bits on a synchronous MTE tag check fault.

This feature is supported in AArch64 state only.

FEAT\_MTE\_TAGGED\_FAR is OPTIONAL.

If FEAT\_MTE\_TAGGED\_FAR is implemented, then FEAT\_MTE4 is implemented.

The following field identifies the presence of FEAT\_MTE\_TAGGED\_FAR:

- ID\_AA64PFR2\_EL1.MTEFAR.

## FEAT\_PCSRv8p9, Armv8.9 PC Sample-based Profiling Extension

FEAT\_PCSRv8p9 introduces a mechanism to suspend PC Sample-based Profiling.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_PCSRv8p9 is OPTIONAL from Armv8.8.

If FEAT\_PCSRv8p9 is implemented, then FEAT\_PCSRv8p2 is implemented.

The following field identifies the presence of FEAT\_PCSRv8p9:

- PMDEVID.PCSample.

For more information, see Suspending and activating PC Sample-based Profiling.

## FEAT\_PFAR, Physical Fault Address Register Extension

FEAT\_PFAR introduces the Physical Fault Address Registers, PFAR\_ELx, that record the faulting physical address for a synchronous External abort or SError exception.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_PFAR is OPTIONAL from Armv8.8.

When FEAT\_AA64 and FEAT\_PFAR are implemented, FEAT\_AA64EL1 is implemented.

When FEAT\_PFAR and FEAT\_AA64EL2 are implemented, FEAT\_FGT2 is implemented.

The following field identifies the presence of FEAT\_PFAR:

- ID\_AA64PFR1\_EL1.PFAR.

## FEAT\_PMUv3\_EDGE, PMU event edge detection

FEAT\_PMUv3\_EDGE introduces edge-detection logic to support counting threshold crossing events.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_PMUv3\_EDGE is OPTIONAL from Armv8.8.

If FEAT\_PMUv3\_EDGE is implemented, then FEAT\_PMUv3\_TH is implemented.

The following fields identify the presence of FEAT\_PMUv3\_EDGE:

- PMMIR\_EL1.EDGE.
- PMMIR.EDGE.
- PMMIR.EDGE.

For more information, see Event threshold and edge counting.

## FEAT\_PMUv3\_ICNTR, Fixed-function instruction counter

FEAT\_PMUv3\_ICNTR introduces a fixed-function instruction counter to the PMU.

This feature is supported in both AArch64 and AArch32 states. The counter is not accessible from AArch32 state.

FEAT\_PMUv3\_ICNTR is OPTIONAL from Armv8.8.

If FEAT\_PMUv3\_ICNTR is implemented, then FEAT\_PMUv3p9 is implemented.

When FEAT\_PMUv3\_ICNTR and FEAT\_AA64EL2 are implemented, FEAT\_FGT2 is implemented.

The following fields identify the presence of FEAT\_PMUv3\_ICNTR:

- ID\_AA64DFR1\_EL1.PMICNTR.
- PMCFGR.NCG.

For more information, see About the Performance Monitors.

## FEAT\_PMUv3\_SS, PMU Snapshot extension

FEAT\_PMUv3\_SS defines an IMPLEMENTATION DEFINED Snapshot Extension, compatible with the CoreSight PMU Snapshot Extension.

This feature is supported in both AArch64 and AArch32 states. The PMU snapshot registers are not accessible from AArch32 state.

FEAT\_PMUv3\_SS is OPTIONAL from Armv8.8.

If FEAT\_PMUv3\_SS is implemented, then FEAT\_PMUv3p9 is implemented.

When FEAT\_PMUv3\_SS and FEAT\_AA64EL2 are implemented, FEAT\_FGT2 is implemented.

If FEAT\_PMUv3\_SS is implemented, then FEAT\_AA32EL1 is not implemented.

The following fields identify the presence of FEAT\_PMUv3\_SS:

- ID\_AA64DFR0\_EL1.PMSS.
- PMDEVID.PMSS.

For more information, see PMU snapshots.

## FEAT\_PMUv3p9, Armv8.9 PMU extensions

FEAT\_PMUv3p9 introduces the following to the Performance Monitors Extension:

- Provides finer-grained control over allocation of PMU event counters to an EL0 process.
- Allows an arbitrary combination of event counters and fixed-function counters to be zeroed.
- Provides controls to configure the PMU to directly request the PE enters Debug state without using the CTI.
- Updates PMU event definitions.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_PMUv3p9 is OPTIONAL from Armv8.8.

In an Armv8.9 implementation, if FEAT\_PMUv3 is implemented, FEAT\_PMUv3p9 is implemented.

If FEAT\_PMUv3p9 is implemented, then FEAT\_PMUv3p8 is implemented.

When FEAT\_PMUv3p9 and FEAT\_AA64EL2 are implemented, FEAT\_FGT2 is implemented.

The following fields identify the presence of FEAT\_PMUv3p9:

- ID\_AA64DFR0\_EL1.PMUVer.
- ID\_DFR0\_EL1.PerfMon.
- ID\_DFR0.PerfMon.
- EDDFR.PMUVer.

For more information, see:

- PMUOverflow external debug request.
- EL0 access controls.
- PMUEvent Descriptions.
- Resetting counters.

## FEAT\_PRFMSLC, SLC target support for PRFM and PRFUM instructions

FEAT\_PRFMSLC introduces a system level cache option for the PRFM and PRFUM instructions.

This feature is supported in AArch64 state only.

FEAT\_PRFMSLC is OPTIONAL from Armv8.0.

The following field identifies the presence of FEAT\_PRFMSLC:

- ID\_AA64ISAR2\_EL1.PRFMSLC.

## FEAT\_RASv2, RAS Extension v2

FEAT\_RASv2 introduces the following to the Reliability, Availability, and Serviceability Extension:

- The features defined by FEAT\_RASSAv2 in the System register error records.
- The error group status register, ERXGSR\_EL1.
- Acontrol to trap writes to RAS error record System registers to EL3.
- An additional syndrome to ESR\_ELx for error exceptions.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_RASv2 is OPTIONAL from Armv8.8.

In an Armv8.9 implementation, if FEAT\_RAS is implemented, FEAT\_RASv2 is implemented.

When FEAT\_RASv2 and FEAT\_AA64EL2 are implemented, FEAT\_FGT2 is implemented.

If FEAT\_RASv2 is implemented, then FEAT\_RASv1p1 is implemented.

If FEAT\_RASv2 is implemented, then FEAT\_RASSAv2 is implemented.

The following fields identify the presence of FEAT\_RASv2:

- ID\_AA64PFR0\_EL1.RAS.
- ID\_PFR0\_EL1.RAS.
- ID\_PFR0.RAS.

For more information, see:

- RAS PE architecture.
- Arm ® Reliability Availability and Serviceability (RAS) System Architecture, for A-profile architecture (ARM IHI 0100).

## FEAT\_RPRFM, Support for Range Prefetch Memory instruction

FEAT\_RPRFM introduces the Range Prefetch Memory hint instruction, RPRFM which specifies the range of addresses that are likely to be accessed in the near future and their expected reuse.

This feature is supported in AArch64 state only.

FEAT\_RPRFM is OPTIONAL from Armv8.0.

The following field identifies the presence of FEAT\_RPRFM:

- ID\_AA64ISAR2\_EL1.RPRFM.

## FEAT\_S1PIE, Stage 1 permission indirections

FEAT\_S1PIE introduces a way to set stage 1 permissions that allows more efficient use of the permission bits in translation table descriptors and provides the ability to introduce additional permission types.

This feature is supported in AArch64 state only.

FEAT\_S1PIE is OPTIONAL from Armv8.8.

If FEAT\_S1PIE is implemented, then FEAT\_ATS1A is implemented.

If FEAT\_S1PIE is implemented, then FEAT\_TCR2 is implemented.

The following field identifies the presence of FEAT\_S1PIE:

- ID\_AA64MMFR3\_EL1.S1PIE.

For more information, see Stage 1 Indirect permissions.

## FEAT\_S1POE, Stage 1 permission overlays

FEAT\_S1POE allows stage 1 permissions to be progressively restricted by processes running at EL0 without requiring TLB maintenance, and reduces the number of calls to privileged software.

This feature is supported in AArch64 state only.

FEAT\_S1POE is OPTIONAL from Armv8.8.

If FEAT\_S1POE is implemented, then FEAT\_TCR2 is implemented.

If FEAT\_S1POE is implemented, then FEAT\_ATS1A is implemented.

If FEAT\_S1POE is implemented, then FEAT\_HPDS is implemented.

The following field identifies the presence of FEAT\_S1POE:

- ID\_AA64MMFR3\_EL1.S1POE.

For more information, see Stage 1 Overlay permissions.

## FEAT\_S2PIE, Stage 2 permission indirections

FEAT\_S2PIE introduces all of the following:

- Amethod to set stage 2 permissions that allows more efficient use of the permission bits in translation table descriptors and provides the ability to introduce additional permission types.
- The Mostly Read Only (MRO) permission in stage 2 translations.

This feature is supported in AArch64 state only.

FEAT\_S2PIE is OPTIONAL from Armv8.8.

If FEAT\_S2PIE is implemented, then FEAT\_EL2 is implemented.

The following field identifies the presence of FEAT\_S2PIE:

- ID\_AA64MMFR3\_EL1.S2PIE.

For more information, see Stage 2 Indirect permissions.

## FEAT\_S2POE, Stage 2 permission overlays

FEAT\_S2POE provides a mechanism for stage 2 permissions to be progressively restricted, such that different EL1&amp;0 contexts that are using the same stage 2 translation tables can be provided with different sets of permissions.

This feature is supported in AArch64 state only.

FEAT\_S2POE is OPTIONAL from Armv8.8.

If FEAT\_S2POE is implemented, then FEAT\_EL2 is implemented.

If FEAT\_S2POE is implemented, then FEAT\_S2PIE is implemented.

The following field identifies the presence of FEAT\_S2POE:

- ID\_AA64MMFR3\_EL1.S2POE.

For more information, see Stage 2 Overlay permissions.

## FEAT\_SPECRES2, Enhanced speculation restriction instructions

FEAT\_SPECRES2 introduces a speculation restriction instruction, Clear Other Speculative Prediction Restriction by Context (COSP), to the instructions that are part of FEAT\_SPECRES.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_SPECRES2 is OPTIONAL from Armv8.0.

FEAT\_SPECRES2 is mandatory from Armv8.9.

The following fields identify the presence of FEAT\_SPECRES2:

- ID\_AA64ISAR1\_EL1.SPECRES.
- ID\_ISAR6\_EL1.SPECRES.
- ID\_ISAR6.SPECRES.

For more information, see:

- Prediction restriction instructions.
- Execution, data prediction and prefetching restriction System instructions.
- Execution and data prediction restriction System instructions.

## FEAT\_SPE\_CRR, Statistical Profiling call return branch records

FEAT\_SPE\_CRR extends the Operation Type packet to provide more information whether the branch is a procedure call or a procedure return.

This feature is supported in AArch64 state only.

FEAT\_SPE\_CRR is OPTIONAL.

In an Armv8.9 implementation, if FEAT\_SPE is implemented, FEAT\_SPE\_CRR is implemented.

If FEAT\_SPE\_CRR is implemented, then FEAT\_SPEv1p4 is implemented.

If FEAT\_SPE and FEAT\_GCS are implemented, then FEAT\_SPE\_CRR is implemented.

The following field identifies the presence of FEAT\_SPE\_CRR:

- PMSIDR\_EL1.CRR.

## FEAT\_SPE\_DPFZS, Disable Cycle Counter on SPE Freeze

FEAT\_SPE\_DPFZS introduces controls to disable cycle counting when event counting is frozen on a Statistical Profiling Buffer Management event.

This feature is supported in AArch64 state only.

FEAT\_SPE\_DPFZS is OPTIONAL from Armv8.6.

If FEAT\_PMUv3p9 and FEAT\_SPEv1p4 are implemented, then FEAT\_SPE\_DPFZS is implemented.

If FEAT\_SPE\_DPFZS is implemented, then FEAT\_PMUv3p7 and FEAT\_SPEv1p2 are implemented.

The following field identifies the presence of FEAT\_SPE\_DPFZS:

- ID\_AA64DFR1\_EL1.DPFZS.

## FEAT\_SPE\_FDS, Statistical Profiling data source filtering

FEAT\_SPE\_FDS provides the capability to filter sample records by all or part of the sampled Data Source packet.

This feature is supported in AArch64 state only.

FEAT\_SPE\_FDS is OPTIONAL from Armv8.8.

In an Armv8.9 implementation, if FEAT\_SPE\_LDS is implemented, FEAT\_SPE\_FDS is implemented.

If FEAT\_SPE\_FDS is implemented, then FEAT\_SPE\_LDS is implemented.

If FEAT\_SPE\_FDS is implemented, then FEAT\_SPEv1p4 is implemented.

When FEAT\_SPE\_FDS and FEAT\_AA64EL2 are implemented, FEAT\_FGT2 is implemented.

The following field identifies the presence of FEAT\_SPE\_FDS:

- PMSIDR\_EL1.FDS.

For more information, see Filtering sample records.

## FEAT\_SPEv1p4, Statistical Profiling Extension version 1.4

FEAT\_SPEv1p4 introduces the following to the Statistical Profiling Extension:

- Additions to the Events packet to provide more information about the data source.
- Additional event-based record filtering control bits in PMSEVFR\_EL1 and PMSNEVFR\_EL1 that add the ability to filter by additional existing bits in the Events packet.

This feature is supported in AArch64 state only.

FEAT\_SPEv1p4 is OPTIONAL from Armv8.8.

In an Armv8.9 implementation, if FEAT\_SPE is implemented, FEAT\_SPEv1p4 is implemented.

If FEAT\_SPEv1p4 is implemented, then FEAT\_SPEv1p3 is implemented.

The following field identifies the presence of FEAT\_SPEv1p4:

- ID\_AA64DFR0\_EL1.PMSVer.

## FEAT\_SPMU, System Performance Monitors Extension

FEAT\_SPMU provides a framework of architectural System registers and behaviors for System PMUs, which are PMUs other than the Performance Monitors Extension PMU, that are accessible by the PE.

This feature is supported in both AArch64 and AArch32 states.

FEAT\_SPMU is OPTIONAL from Armv8.8.

If FEAT\_SPMU is implemented, then FEAT\_PMUv3p9 is implemented.

When FEAT\_SPMU and FEAT\_AA64EL2 are implemented, FEAT\_FGT2 is implemented.

The following field identifies the presence of FEAT\_SPMU:

- ID\_AA64DFR1\_EL1.SPMU.

For more information, see System Performance Monitors Extension.

## FEAT\_THE, Translation Hardening Extension

FEAT\_THE provides a mechanism to prevent modification of an arbitrary subset of translation table entries from within the exception level that owns the translation tables, and introduces the following:

- The stage 1 Assured Translation property and the stage 2 AssuredOnly property.
- Stage 2 TopLevel checks.
- Read-Check-Write instructions, RCW* and RCWS*.
- Read-Check-Write mask registers, RCWMASK\_EL1 and RCWSMASK\_EL1.
- The Protected attribute in stage 1 descriptors.

This feature is supported in AArch64 state only.

FEAT\_THE is OPTIONAL from Armv8.8.

When FEAT\_THE and FEAT\_AA64EL2 are implemented, FEAT\_S2PIE is implemented.

When FEAT\_THE and FEAT\_AA64EL2 are implemented, FEAT\_FGT2 is implemented.

If FEAT\_THE is implemented, then FEAT\_TCR2 is implemented.

The following field identifies the presence of FEAT\_THE:

- ID\_AA64PFR1\_EL1.THE.

For more information, see:

- Translation Hardening Extension.
- Read-Check-Write.