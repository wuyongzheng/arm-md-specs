## 13.2 SMMU disabled global bypass attributes

When the SMMU is disabled for a given Security state, transactions that belong to that Security state are subject to global bypass attribute overrides.

Figure 13.2: Input attribute flow - SMMU disabled bypass and start of translation flow

<!-- image -->

When SMMU\_S\_IDR1.SECURE\_IMPL == 0 and SMMU\_CR0.SMMUEN == 0, all untranslated transactions bypass the translation and configuration facilities of the SMMU. The memory type, Shareability, Read/Write allocate, Transient, Inst/Data and Privilege attributes of the transaction might be individually replaced by the MTCFG/MemAttr, SHCFG, ALLOCCFG, INSTCFG and PRIVCFG override fields of the SMMU\_GBPA register, respectively. Each attribute might take a set value or select to Use incoming. In the latter case, the attribute is either taken from the incoming interconnect or, when not supplied, the default input attribute constructed in the

SMMU. Apart from these overrides, the transaction is output directly. For some classes of transaction, for example Cache Maintenance Operations, the SMMU may apply protocol-specific normalization on the output transaction attributes.

Note: When the SMMU is disabled, ATS Translation Requests and ATS-translated transactions are terminated by the SMMU. See section 3.9.1.2 Responses to ATS Translation Requests .

Alternatively, when SMMU\_S\_IDR1.SECURE\_IMPL == 0 and SMMU\_CR0.SMMUEN == 1, an STE is located and the translation flow begins.

When SMMU\_S\_IDR1.SECURE\_IMPL == 1, the behavior of a transaction on arrival at the SMMU is determined by the Security state of its StreamID, as determined by the SEC\_SID input, see section 3.10.1 StreamID Security state (SEC\_SID) . If the stream is Non-secure and SMMU\_CR0.SMMUEN == 0, the attributes are overridden by SMMU\_GBPA as described earlier in this section. If the stream is Secure and SMMU\_S\_CR0.SMMUEN == 0, the attributes are determined by SMMU\_S\_GBPA in the same way, otherwise a Secure STE is located and the translation flow begins. The output NS attribute is determined by SMMU\_S\_GBPA.NSCFG, it can use the incoming value or be overridden to either state.

The reset state of the bypass attribute register SMMU\_GBPA, and when SMMU\_S\_IDR1.SECURE\_IMPL == 1 SMMU\_S\_GBPA, is IMPLEMENTATION DEFINED.

Note: The SMMU might provide an implementation-time configuration of the default bypass attributes which allows a system designer to ensure that device DMA has useful attributes even if system software has not initialized the SMMU.

Arm recommends that the default attributes are set as appropriate for the system in accordance with relevant base system architecture definitions.

This case is illustrated by this pseudocode:

```
// See 13.1.3: Attrs input_attrs = add_defaults_for_unsupplied(upstream_attrs); bool secure = (SEC_SID == SEC_SID_Secure); if (secure) { output_attrs = replace_attrs(SMMU_S_GBPA, input_attrs); } else { output_attrs = replace_attrs(SMMU_GBPA, input_attrs); output_attrs.NS = 1; } // MT, SH, RA, WA, TR, INST, PRIV are unchanged or overridden, // depending on respective register field. // // NS is unchanged or overridden if secure stream, otherwise // fixed at 1. // See 13.1.7: output_attrs = ensure_consistent_attrs(output_attrs);
```