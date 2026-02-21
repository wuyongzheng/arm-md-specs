## 13.4 Normal translation flow

Figure 13.3: Attribute determination in translation

<!-- image -->

When the StreamID of a transaction selects an STE configuration with two stages of translation, the memory attribute of the transaction is determined by the stage 1 AttrIndex descriptor attribute and the MAIR fields, and combined with the stage 2 MemAttr descriptor attribute. For stage 1-only translations, the memory attributes are determined solely by the stage 1 descriptor attributes. For stage 2-only translations, the memory attributes are determined by the input attribute, with STE overrides, combined with the stage 2 descriptor attributes.

First, the incoming attributes, with defaults constructed for any unsupplied attributes, are subject to the STE

override described in section 13.3 Translation flow, STE bypasses stage 1 and stage 2 . These attributes are provided to the first enabled stage of translation. If stage 1 bypasses, these attributes are provided to stage 2 directly.

If stage 1 translates, the stage 1 descriptor, in combination with the MAIR fields of the CD, determine the stage 1 attributes and page permissions. The R/W, PRIV and INST attributes, as modified by STE overrides, are checked against the page permissions.

## 13.4.1 Stage 1 page permissions

When using the Direct Permission Scheme for stage 1, the effect of the lower bit of the stage 1 descriptor AP[2:1] field, AP[1], changes depending on the translation regime under which the translation is performed, as determined by StreamWorld. For EL1 or for any-EL2-E2H, the AP[1] bit controls the EL0 access permissions of the page (PRIV == 0). However, when StreamWorld == any-EL2 or StreamWorld == EL3, the AP[1] bit is ignored and treated as if it were 1. This has the same effect as treating PRIV == 1 for the purposes of permission checking, which means that input PRIV attributes and any STE.PRIVCFG overrides are ignored for these checks.

When PRIV and INST attributes are output to the memory system, they are presented as the result of applying the STE.PRIVCFG and STE.INSTCFG overrides to the input attribute. They are not modified after this point.

See section 3.26.1 Stage 1 permission indirections for when stage 1 is configured to use the Indirect Permission Scheme.

## 13.4.2 Stage 1 memory attributes

The attributes determined from the stage 1 translation table descriptor and CD.MAIR are provided directly to the stage 2 translation. The incoming attributes, including any STE overrides, are discarded and replaced by the stage 1 attributes, with the exception of RA/WA/TR.

When the translation is from a Secure StreamID, the target IPA or PA space from stage 1 is determined directly from the effective NS bit of the descriptor, which must take into account the value of NSTable flags on intermediate Table descriptors in addition to the final descriptor NS flag, in the same way as on the PE. In addition, CDs that are used with Secure streams contain NSCFGx flags that determine the starting NS attribute of translation table walks performed through CD.TTB0/1. When a translation is fetched using a CD.TTB0/1 with a corresponding NSCFGx == 1, the stage 1 targets Non-secure IPA or PA space. When a translation is from a Non-secure stream, the output NS attribute that is output is always 1 and the NS attribute that was input with the transactions is ignored.

When Secure stage 2 is supported and enabled, the final transaction NS bit depends on the configuration of the stage 2 IPA space, STE.{S2NSA, S2NSW, S2SA, S2SW}. See section 3.10.2.2 Secure EL2 and support for Secure stage 2 translation . Otherwise, the final transaction uses the target IPA space from stage 1, or stage 1 bypass.

Note: The behavior of the input NS attribute in a stage 1-only configuration matches the SMMUv2 [4] behavior in that the input NS attribute is wholly determined by the stage 1 descriptor and translation table walk configuration. The input NS attribute and STE override only affect the target IPA or PA space when no stage 1 translation is configured.

When the attribute input to stage 1 is a Normal-cacheable type, the RA/WA/TR attributes are not discarded and instead are combined with those determined from the stage 1 translation descriptor and MAIR. Any other type does not communicate RA/WA/TR hints, in which case the stage 1 translation RA/WA/TR attributes are used directly. All other attributes must be overridden by stage 1 translation table attributes.

Note: This property, combined with STE.ALLOCCFG == 0b0xxx configuration, allows a client device to influence per-transaction allocation/transient attributes when using stage 1 translation tables, allowing sub-page control.

## 13.4.3 Stage 2

If stage 2 bypasses, the attributes provided by the incoming transaction or the stage 1 translation are forwarded unchanged to the memory system.

If stage 2 translates, the MT and SH attributes input to stage 2 undergo a combine operation with the stage 2

translation descriptor attributes to produce the output attributes. If STE.S2FWB == 1, then the combine operation uses the encoding and behavior of the stage 2 translation descriptor attributes for the FWB feature as described in Armv8.4 [2].

Stage 2 descriptors do not include read/write allocate or transient hints so the RA/WA/TR attributes provided to stage 2 are passed on unchanged.

The INST attribute is checked, along with R/W, to evaluate stage 2 permissions. If SMMU\_IDR3.XNX == 0, the PRIV attribute is not used to evaluate stage 2 permissions. If SMMU\_IDR3.XNX == 1, the PRIV attribute is used to evaluate stage 2 permissions.

When using the Direct Permission Scheme, stage 2 checks are performed against the descriptor page permissions.

See section 3.26.2 Stage 2 permission indirections for when stage 2 is configured to use the Indirect Permission Scheme.

## 13.4.4 Output

The transaction is output after ensuring consistency of the attributes and forcing NS == 1 for transactions on Non-secure streams.

Pseudocode, which also illustrates the cases describe in sections 13.2 SMMU disabled global bypass attributes and 13.3 Translation flow, STE bypasses stage 1 and stage 2 in more detail, is show below:

```
// See 13.1.3: Attrs input_attrs = add_defaults_for_unsupplied(upstream_attrs); bool secure = (SEC_SID == SEC_SID_Secure); if (secure && SMMU_S_CR0.SMMUEN == 0) { output_attrs = replace_attrs(SMMU_S_GBPA, input_attrs); // See 13.1.7: output_attrs = ensure_consistent_attrs(output_attrs); output_transaction(output_attrs); // Address, direction not shown // Done. } // Else carry on below if (!secure && SMMU_CR0.SMMUEN == 0) { output_attrs = replace_attrs(SMMU_GBPA, input_attrs); output_attrs.NS = 1; // See 13.1.7: output_attrs = ensure_consistent_attrs(output_attrs); output_transaction(output_attrs); // Address, direction not shown // Done. } // Else carry on below // If we get to here, the appropriate SMMU interface is enabled and // configuration can be fetched: STE ste = get_STE_for_stream(StreamID); Attrs i; // Starting attributes are as input, with STE overrides: i = replace_attrs(ste, input_attrs); if (ste.s1_translates()) { Attrs s1_attrs; TTD s1_ttd; CD cd = get_CD(ste, StreamID, SubstreamID, SubstreamID_valid); s1_ttd = s1_translation(cd, ste); // Address not shown; IPA determined from VA. NS of stage 1 translation // table walk depends on CD.NSCONFIGx and is not shown here. s1_attrs = s1_ttd.lookup_attrs(); // The returned s1_attrs contains attributes determined from the
```

```
// translation descriptor and MAIR, including RA/WA and TR. if (s1_ttd.translation_fault()) { // XXXX Stage 1 translation fault // Note: A speculative read transaction is simply terminated // with abort here, without recording an event. } // Note: Permission checking must consider HTTU configuration, // and update Access flag and Dirty state instead of signaling a related fault // when HTTU enabled: if (check_perms_and_httu(cd, s1_ttd, i.RW, i.INST, i.PRIV) == FAULT) { // XXXX Stage 1 permissions or Access flag fault // Note: EL2 or AArch64 EL3 stage 1 do not check PRIV, // i.e. client traffic behaves as if PRIV == 1. However, // the PRIV attribute is not modified. } // Note: See section 13.4.2; when a cached type is input to Stage 1, // s1_attrs.{RA,WA,TR} are combined with i.{RA,WA,TR} instead of // replacement (non-cached/Device types do not express RA/WA/TR // attributes): if (is_cached_type(i.MT)) { i.{RA,WA,TR} = combine_attrs(i.{RA,WA,TR}, s1_attrs.{RA,WA,TR}); } else { // An input NC/Device type does not provide these attributes, // so take these attributes from S1: i.{RA,WA,TR} = s1_attrs.{RA,WA,TR}; } // MT and SH are taken directly from Stage 1: i.{MT,SH} = s1_attrs.{MT,SH}; // NS is taken from the 'effective' value calculated from // S1 Block or Page descriptor, CD.NSCONFIGx and appropriate NSTable bits: i.NS = s1_ttd.get_effective_NS(); // RW, INST, PRIV do not change. } else { // MT, SH, RA, WA, TR unchanged; and RW, INST, PRIV, NS // permissions passed through. } if (ste.s2_translates()) { Attrs s2_attrs; TTD s2_ttd; // Fetch stage 2 translation table descriptor. // Address not shown; PA determined from IPA and HTTU is performed. if (secure) { // Perform S-IPA or NS-IPA translation table walk with given NS: bool sipa_s2_ttw_ns = ste.S2SW; bool nsipa_s2_ttw_ns = ste.S2NSW; // Final NS is a function of the walk NS: bool sipa_ns = sipa_s2_ttw_ns || ste.S2SA; bool nsipa_ns = nsipa_s2_ttw_ns || sipa_ns || ste.S2NSA; // The NS input to stage 2 indicates the NS or S IPA space. if (i.NS) { s2_ttd = s2_translation_ns_ipa(ste, nsipa_s2_ttw_ns); i.NS = nsipa_ns; } else { s2_ttd = s2_translation_s_ipa(ste, sipa_s2_ttw_ns); i.NS = sipa_ns; } } else { // Non-secure stream
```

```
s2_ttd = s2_translation(ste); } s2_attrs = s2_ttd.lookup_attrs(); if (s2_ttd.translation_fault()) { // XXX Stage 2 translation fault // Note: On any fault, a speculative read transaction is simply // terminated with abort. // Note: HTTU at Stage 1 is permitted, even if we fault @S2 } // S2 does not encode RA/WA/TR; these values plus combine_attrs() below // result in "take input from S1/previous step" behavior for RA/WA/TR: s2_attrs.RA_inner = true; s2_attrs.RA_outer = true; s2_attrs.WA_inner = true; s2_attrs.WA_outer = true; s2_attrs.TR_inner = false; s2_attrs.TR_outer = false; if (s2_ttd.S2FWB == 0) { // MT, SH, RA, WA, TR updated via combine: i = combine_attrs(i, s2_attrs); } else { // combine_attrs_fwb() treats the encoding of stage 2 // attribues as defined for the FWB features in Armv8.4 i = combine_attrs_fwb(i, s2_attrs); } // See HTTU note in Stage 1: if (check_perms_and_httu(ste, s2_ttd, i.RW, i.INST, i.PRIV) == FAULT) { // XXXX Stage 2 permissions or Access flag fault // Note: S2 checks PRIV if SMMU_IDR3.XNX == 1. } } else { // MT, SH, RA, WA, TR unchanged; and RW, INST, PRIV, NS // permissions passed through. } // Finally, a Non-secure stream is not permitted to output NS == 0; // the overrides and page attribute are ignored: if (!secure) { output_attrs.NS = 1; } // MT, SH, RA, WA, TR may be modified by translations and overrides. // INST, PRIV may be modified by STE overrides. // // For a secure stream, stage 1 output NS is determined from the Stage 1 // translation (if present), otherwise is the STE override or input value. // This is used to select an IPA space in stage 2, or output directly if no // stage 2. // See 13.1.7: output_attrs = ensure_consistent_attrs(output_attrs); output_transaction(output_attrs); // Address, direction not shown // Done.
```