## G5.14 Pseudocode description of VMSAv8-32 memory system operations

This section contains a list of pseudocode functions describing VMSAv8-32 memory operations. The following subsections describe the pseudocode functions:

- Full Physical Address.
- Translation regime.
- Address translation.
- Long-descriptor Translation table walk.
- Short-descriptor Translation table walk.
- Memory attribute decoding.
- Fault detection.

See also the descriptions of pseudocode for general memory system operations in Pseudocode description of general memory System instructions.

## G5.14.1 Full Physical Address

Acomplete physical address necessary to identify a location in physical memory is captured by the type FullAddress . This is composed of:

- Abitstring address, which identifies the physical address.
- An enumeration paspace , which identifies the physical address space.

## G5.14.2 Translation regime

The architecture specifies translation regimes in terms of Privilege Level (PL). An alternative approach is used in pseudocode where regimes are expressed in terms of Exception Levels instead, mirroring regimes in AArch64. The pseudocode and ARM use a differently named but equivalent set of regimes:

Table G5-36 Pseudocode and equivalent ARM regimes

| Pseudocode Regime   | Equivalent ARM regime                                |
|---------------------|------------------------------------------------------|
| Regime_EL10         | Secure PL1&0 when EL3 is AArch64 or Non-Secure PL1&0 |
| Regime_EL30         | Secure PL1&0 when EL3 is AArch32                     |
| Regime_EL2          | Non-Secure PL2                                       |

## G5.14.3 Address translation

AArch32.TranslateAddress() acts as the entry point to VMSAv8-32 and performs the required address translation based on the provided parameters and system register configurations. The function returns an AddressDescriptor structure holding valid data for either of the following:

- Target memory address and attributes for a non-faulting translation.
- Fault details holding data to be populated in syndrome registers.

AArch32.FullTranslate() selects the translation regime and performs first and potentially second stage of translation returning the physical address (PA) and attributes of target memory. AArch32.S1TranslateSD() carries out the first stage of translation when stage 1 is not disabled and Long-descriptor format is used, mapping the virtual address (VA) to the intermediate physical address (IPA) and carrying out permission checks. Alternatively AArch32.S1TranslateSD() carries out the first stage of translation using the Short-descriptor format along with

Domain checks and TEX memory attribute mapping. Otherwise, AArch32.S1DisabledOutput() assigns the appropriate memory attributes and flat maps the input address to the output address. AArch32.S2Translate() carries out stage 2 translation for Regime\_EL10 when enabled, mapping the IPA to the PA. Otherwise, the IPA is the PA.

## G5.14.4 Long-descriptor Translation table walk

Aseparate walk function is dedicated for Stage 1 Long-descriptor format, AArch32.S1WalkLD() , and Stage 2, AArch32.S2Walk() , which supports only Long-descriptor format. Each use walk parameters extracted from related system registers and held in S1TTWParams for stage 1 and S2TTWParams for stage 2. Parameters are collected based on the active translation regime. For instance, stage 1 EL2 translation regime parameters are obtained and returned by the function AArch32.S1TTWParamsEL2 (). Given these parameters, a walk initializes a walk state of the type TTWState, holding the base address of the first translation table.

The walk progressively fetches and decodes Translation Table descriptors, updating the walk state to the next base address as it descends through the levels of tables until a Block or Page descriptor is discovered or an invalid descriptor is fetched. Decoding the descriptor for both stage 1 and stage 2 walks is carried out by the function AArch32.DecodeDescriptorTypeLD() .

For a non-faulting walk, a valid final walk state is returned, otherwise a faulting walk could report one of the following at a specified level:

- Translation Fault.
- Address Size Fault.
- Access Flag Fault.

## G5.14.5 Short-descriptor Translation table walk

Short-Descriptor format is only supported for Regime\_EL10 and Regime\_EL30 (PL1&amp;0) Stage 1 and a separate walk function is dedicated for that, AArch32.S1WalkSD() . The limited number of parameters are collected in the walk function and would otherwise follow a similar flow to Long-descriptor formats of iteratively updating the walk state. The walk notably collects the domain and Short-descriptor format type which are unique to Short-descriptor formats. The descriptor type is decoded using AArch32.DecodeDescriptorTypeSD() .

For a non-faulting walk, a valid final walk state is returned, otherwise a faulting walk could report one of the following at a specified level:

- Translation Fault.
- Address Size Fault.
- Access Flag Fault (when SCTLR.AFE is configured to support Access flags).

## G5.14.6 Memory attribute decoding

If a stage of translation is enabled, Fetched Leaf descriptors encode memory attributes assigned to the output of translation. Stage 1 Long-descriptor format memory attributes are decoded by the function S1DecodeMemAttrs() . Likewise, stage 2 memory attributes are decoded by the function S2DecodeMemAttrs() followed by combining stage 1 and stage 2 attributes by the function S2CombineS1MemAttrs() . Aseparate set of functions are used to assign memory attributes to the output of Short-descriptor format. AArch32.DefaultTEXDecode() is used when TEX remapping is disabled, otherwise AArch32.RemappedTEXDecode() defines output memory attributes.

## G5.14.7 Fault detection

As soon as translation is invoked, a reserve FaultRecord accompanies the process, capturing the stage and level of translation as it proceeds. When a fault is detected, it is reflected in the FaultRecord and reported back as the result of translation with the most recent state to be reported already captured within. The following functions detect a certain type of fault, their outputs are all boolean with a TRUE value on detection:

- AArch32.S1LDHasPermissionsFault() and AArch32.S2HasPermissionsFault() detect a permissions fault for stage 1 and stage 2 respectively for Long-descriptor format. AArch32.S1SDHasPermissionsFault() detects a permissions fault for a translation in Short-descriptor format. Note that for atomic instructions introduced by FEAT\_LSE, these functions are called twice, once to check for read permissions and another for write allowing the correct failure to be reported.
- AArch32.S1HasAlignmentFaultDueToMemType() and AArch32.S2HasAlignmentFaultDueToMemType() detect an alignment fault for stage 1 and stage 2 respectively.
- AArch32.S2InconsistentSL() detects a stage 2 translation fault caused by erroneous configuration of the VTCR.SL0 field.
- AArch32.VAIsOutOfRange() detects a stage 1 translation fault caused by virtual addresses larger than the address input size configured. Similarly, AArch64.IPAIsOutOfRange() detects a stage 2 translation fault caused by the output of stage 1 being larger than the configured input size for stage 2. Both are solely part of Long-descriptor format translation.

Note

Domain faults are detected inline as part of AArch32.S1TranslateSD() since they are a simple equality check.