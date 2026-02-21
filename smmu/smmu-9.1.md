## 9.1 Register usage

## 9.1.1 ATOS\_CTRL

Software writes ATOS\_CTRL.RUN to 1 to request a translation. The bit is cleared back to 0 by the SMMU when ATOS\_PAR has been updated with the result.

Software must not write any register in the ATOS group when ATOS\_CTRL.RUN == 1.

SMMUEN must not be cleared while one or more ATOS requests are in progress for the programming interface, otherwise ongoing requests might be terminated. ATOS\_CTRL.RUN is cleared by an Update of SMMUEN to 0.

Note: An ATOS request that is made through the Secure programming interface for a Non-secure StreamID might be affected by Non-secure software simultaneously clearing SMMU\_CR0.SMMUEN from another PE, so must accept spurious ATOS translation failures which might result.

See SMMU\_GATOS\_CTRL for more information on ATOS\_CTRL.RUN and alteration of the SMMUEN flags.

## 9.1.2 ATOS\_SID

The StreamID and optional SubstreamID are written to ATOS\_SID.STREAMID, ATOS\_SID.SUBSTREAMID and ATOS\_SID.SSID\_VALID in preparation for a subsequent ATOS lookup. When ATOS\_CTRL.RUN is written to 1, the value of this register is used as input to the process.

The SMMU\_S\_GATOS\_SID register contains a SSEC flag that selects between Secure and Non-secure StreamID lookup for an ATOS request that is issued from the Secure interface. The SSEC flag is RES1 in the SMMU\_S\_VATOS\_SID register. A Secure VATOS request can only access Secure StreamIDs.

Note: Non-secure ATOS interfaces have no SSEC flag, so they can only look up Non-secure StreamIDs.

## 9.1.3 ATOS\_ADDR

The address to be queried is written to ATOS\_ADDR.ADDR.

The type of lookup that is required is written to the ATOS\_ADDR.TYPE field:

| TYPE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00   | Reserved Generates ATOS error INV_REQ.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 0b01   | Stage 1 (Look up IPA/PA from VA) Only format available when SMMUsupports only stage 1 translation. Only format available to VATOS interface. Note: It is permissible to make a stage 1 request for a StreamID with either a stage 1-only or a stage 1 and 2 configuration. Generates ATOS error INV_REQ when SMMUdoes not support stage 1 translation. Generates ATOS error INV_STAGE when stage 1 is supported but not configured to translate for the given StreamID. Note: This does not require a stage 1-only configuration for the StreamID. This lookup returns the stage 1 information from a nested configuration. |

| TYPE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b10   | Stage 2 (look up PA from IPA) Generates ATOS error INV_REQ when used from the SMMU_VATOS_ADDR interface, or when theSMMU does not support stage 2 translation. Generates ATOS error INV_STAGE when stage 2 is supported but not configured to translate for the given StreamID. If SMMU_S_IDR1.SEL2 == 0, generates ATOS error INV_STAGE when issued from the Secure ATOS interface with SMMU_S_GATOS_SID.SSEC == 1. Generates ATOS error INV_REQ if ATOS_SID.SSID_VALID (because no stage 1 translation is requested). Note: This does not require a stage 2-only configuration for the StreamID. This lookup returns the stage 2 information from a nested configuration. |
| 0b11   | Stage 1 and stage 2 (Look up PA from VA) Generates ATOS error INV_REQ when used from SMMU_VATOS_ADDR interface, or when the SMMUdoes not support both stage 1 and stage 2. Generates ATOS error INV_STAGE when stage 1 and stage 2 are supported but not both configured to translate for the given StreamID. If SMMU_S_IDR1.SEL2 == 0, generates ATOS error INV_STAGE when issued from the Secure ATOS interface with SMMU_S_GATOS_SID.SSEC == 1.                                                                                                                                                                                                                          |

When TYPE == 0b01 or 0b11 (requesting stage 1), the generation of INV\_STAGE is determined from whether stage 1 is configured to translate by STE.Config and is not caused by a STE.S1DSS == 0b01 configuration.

A request that is incompatible with the ATOS interface is an invalid request, and results in INV\_REQ.

Note: For example, a stage 1 request to an SMMU that does not support stage 1, or a stage 2 request to a V ATOS interface, will cause INV\_REQ.

A valid request through any ATOS interface for information about a stream that has an invalid STE results in C\_BAD\_STE, if a higher priority fault has not occurred. See section 9.1.4 ATOS\_PAR .

If an STE is fetched successfully and the STE is valid, then one of the following will apply:

- A request through a GATOS interface for information about a stream that has STE.Config == 0b0xx or 0b100 results in INV\_STAGE.
- A request through a VATOS interface for information about a stream that has STE.Config == 0b0xx or 0b100 results in C\_BAD\_STE, because the STE.S2VMID field is not valid and cannot match the VATOS\_SEL.VMID value. See section 9.1.6 SMMU\_(S\_)VATOS\_SEL .

Arequest with ATOS\_SID.SSID\_VALID == 0 on a stream with STE.S1DSS == 0b01 leads to one of the following:

- A stage 1 lookup (TYPE == 0b01 ) behaves according to stage 1-bypass, which returns the address provided in ATOS\_ADDR.ADDR without translation, or returns a stage 1 fault.

If no fault occurs and a result is returned, the result contains the following properties:

- -ATOS\_PAR.ADDR is the input address plus a translation size encoded in conjunction with ATOS\_PAR.Size. The translation size is permitted to be any value between the minimum implemented granule size and the IAS.
- -ATOS\_PAR.ATTR and ATOS\_PAR.SH are IMPLEMENTATION DEFINED.
- -SMMU\_S\_GATOS\_PAR.NS is IMPLEMENTATION DEFINED.

Note: It is possible for an Address Size fault to result from stage 1 in bypass. It is also possible for the configuration of SMMU\_S\_CR0.SIF to cause a stage 1 permission fault on a Secure stream.

- A stage 1 and stage 2 lookup (TYPE == 0b11 ) behaves according to stage 1-bypass, and stage 2-translates, returning the address provided in ATOS\_ADDR.ADDR translated at stage 2, or a stage 1 fault or a stage 2 fault.

The required read/write, instruction/data and privileged/unprivileged properties of the ATOS request are written to ATOS\_ADDR.RnW, ATOS\_ADDR.InD and ATOS\_ADDR.PnU, respectively. These attributes are not affected by the STE.INSTCFG or STE.PRIVCFG overrides.

The required NS attribute of the ATOS request is written to ATOS\_ADDR.NS. The supplied NS attribute is not affected by the STE.NSCFG override.

## 9.1.4 ATOS\_PAR

ATOS\_PAR contains the result of the translation request, which provides either a translated address and attributes or an error result.

The content of ATOS\_PAR is only valid when a translation has been both initiated and completed through the sequence of the corresponding RUN bit having been set to 1 by software, and then cleared to 0 by the SMMU.

If ATOS\_PAR.FAULT == 0, the translation was successful and ATOS\_PAR.ADDR returns the translated address, in addition to the page size, and other fields provide the determined access attributes. See SMMU\_GATOS\_PAR for details of the fields.

The attributes that are returned in ATOS\_PAR.ATTR and ATOS\_PAR.SH are those that are determined from the translation for a stage 1-only or a stage 2-only request or for a stage 1 and stage 2 request. See section 13.1.5 Combine for definition of attribute combination. Because the SH field in the descriptor only encodes a Shareability for Normal memory, a Shareability of OSH is always provided in ATOS\_PAR.SH when a Device memory type is determined from this procedure. The memory attributes do not include STE.{SHCFG, MTCFG, MemAttr} overrides and are permitted to reflect the attributes that are stored in TLB entries. The attributes that are stored in the TLB entries might be an IMPLEMENTATION DEFINED subset of the architectural TTD/MAIR attributes/types, see SMMU\_GATOS\_PAR.

Consistent with the rules for SMMU-originated accesses in a system that supports RME, configuration structure fetches and translation table walks arising from use of the ATOS registers are subject to granule protection checks. See 3.25.3 SMMU-originated accesses .

If a configuration structure fetch or translation table walk fails with a granule protection check fault, this is reported in both:

- The appropriate SMMU\_ROOT\_GPF\_FAR or SMMU\_ROOT\_GPT\_CFG\_FAR register, if that register does not already contain an active fault.
- The appropriate ATOS\_PAR register, as though the failed access experienced an External abort.

When performing an ATOS operation, the SMMU does not perform a granule protection check on the final output address of a successful translation.

If ATOS\_PAR.FAULT == 1, an error or fault occurred during translation. In this case, ATOS\_PAR.FAULTCODE reports whether there was:

- An error in invocation, which is INV\_REQ or INV\_STAGE, as described in section 9.1.3 ATOS\_ADDR .
- A fault or error during translation, corresponding to a standard SMMU event type, for example C\_BAD\_STE or F\_TRANSLATION.
- An internal error. For example, a RAS error that caused the translation to terminate, or the case where SMMUEN was cleared to 0, thereby terminating the translation.

Other fields in ATOS\_PAR determine the following:

- REASON. This field determines whether the issue was encountered at stage 1, or at stage 2 because of the incoming IPA, or because of fetching a stage 1 translation or a CD through an IPA that caused a stage 2 fault.
- FADDR. This field determines the IPA that caused a stage 2 fault.

The validity of the REASON and FADDR fields changes depending on the type of request that is made and the kind of fault encountered. In the following table:

- TRF means any of the Translation Related Faults (F\_TRANSLATION, F\_ADDR\_SIZE, F\_ACCESS, F\_PERMISSION).

- MISC means all other faults, with the exception of F\_WALK\_EABT, F\_CD\_FETCH, INV\_REQ and INV\_STAGE.

Note: MISC therefore represents: INTERNAL\_ERR, C\_BAD\_STREAMID, F\_STE\_FETCH, F\_VMS\_FETCH, C\_BAD\_STE, F\_STREAM\_DISABLED, C\_BAD\_SUBSTREAMID, C\_BAD\_CD, F\_TLB\_CONFLICT, F\_CFG\_CONFLICT.

Note: There are no ATOS changes arising from the introduction of the F\_PERMISSION fields DirtyBit and AssuredOnly in SMMUv3.4. An ATOS operation that fails because of a Permission fault is reported using the existing ATOS\_PAR encodings for Permission faults, regardless of whether the permission fault would be reported with DirtyBit set to 1 or AssuredOnly set to 1 in an F\_PERMISSION event.

| ATOS_ADDR. TYPE                        | Possible FAULTCODE values                                                                | Possible PAR.REASON values   |   FADDR contents | Notes                                                                               |
|----------------------------------------|------------------------------------------------------------------------------------------|------------------------------|------------------|-------------------------------------------------------------------------------------|
| Any                                    | INV_REQ, INV_STAGE                                                                       | 0b00                         |                0 | Error in invocation. See section 9.1.3 ATOS_ADDR                                    |
| 0b01 (stage 1) on stage 1-only stream  | F_WALK_EABT                                                                              | 0b00 (S1)                    |                0 | descriptor fetch abort                                                              |
| 0b01 (stage 1) on stage 1-only stream  | F_CD_FETCH                                                                               | 0b00 (S1)                    |                0 | CD fetch abort                                                                      |
| 0b01 (stage 1) on stage 1-only stream  | TRF, MISC                                                                                | 0b00 (S1)                    |                0 |                                                                                     |
| 0b01 (stage 1) on stage 1 and 2 stream | F_WALK_EABT                                                                              | 0b00 (S1)                    |                0 | Stage 1 descriptor fetch abort (actual bus abort)                                   |
| 0b01 (stage 1) on stage 1 and 2 stream | F_CD_FETCH                                                                               | 0b00 (S1)                    |                0 | CD fetch abort (actual bus abort)                                                   |
| 0b01 (stage 1) on stage 1 and 2 stream | F_CD_FETCH, if stage 2 F_WALK_EABT or stage 2 TRF is caused by CD fetch                  | 0b00 (S1)                    |                0 | CD fetch abort (synthetic, because of a stage 2 translation failure)                |
| 0b01 (stage 1) on stage 1 and 2 stream | F_WALK_EABT, if stage 2 F_WALK_EABT or stage 2 TRF is cased by stage 1 descriptor fetch. | 0b00 (S1)                    |                0 | Stage 1 descriptor fetch abort (synthetic because of a stage 2 translation failure) |

| ATOS_ADDR. TYPE            | Possible FAULTCODE values                                | Possible PAR.REASON values   | FADDR contents                            | Notes                                                                                                                                                                                                       |
|----------------------------|----------------------------------------------------------|------------------------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                            | TRF, MISC                                                |                              |                                           | Configuration or miscellaneous fault, or stage 1 TRF. Note: The IPA that is determined from a Stage 1 translation is not further translated to a PA, therefore stage 2 TRFs on an illegal IPA do not occur. |
| 0b10 (stage 2)             | F_ADDR_SIZE                                              | 0b11 (S2, IN)                | 0                                         | Stage 2 Address Size fault.                                                                                                                                                                                 |
|                            | F_ADDR_SIZE                                              | 0b00 (S1)                    | 0                                         | Stage 1 Address Size fault. It is IMPLEMENTATION DEFINED whether an SMMUv3.0 implementation reports this fault as REASON = 0b00 or 0b01                                                                     |
|                            | F_TRANSLATION, F_ACCESS, F_PERMISSION, F_WALK_EABT, MISC | 0b11 (S2, IN)                | 0                                         |                                                                                                                                                                                                             |
| 0b11 (stage 1 and stage 2) | TRF                                                      | 0b00 (S1)                    | 0                                         | Stage 1 translation- related fault                                                                                                                                                                          |
|                            |                                                          | 0b01 (S2, CD fetch)          | IPA input to stage 2 (CD address)         | Stage 2 fault on CD fetch                                                                                                                                                                                   |
|                            |                                                          | 0b10 (S2, TT fetch)          | IPA input to stage 2 (descriptor address) | Stage 2 fault on stage 1 descriptor fetch                                                                                                                                                                   |
|                            |                                                          | 0b11 (S2, IN)                | IPA input to stage 2 (stage 1 output)     | Stage 2 fault on IPA                                                                                                                                                                                        |
|                            | F_WALK_EABT                                              | 0b00                         | 0                                         | Stage 1 descriptor fetch abort                                                                                                                                                                              |

| ATOS_ADDR. TYPE   | Possible FAULTCODE values   | Possible PAR.REASON values   |   FADDR contents | Notes                                                                              |
|-------------------|-----------------------------|------------------------------|------------------|------------------------------------------------------------------------------------|
|                   |                             | 0b01 , 0b10 , 0b11           |                0 | Stage 2 descriptor fetch abort (for CD/TT/IN, as as indicated by the REASON field) |
|                   | F_CD_FETCH                  | 0b00                         |                0 | CD fetch abort                                                                     |
|                   | MISC                        | 0b00                         |                0 |                                                                                    |

## 9.1.5 ATOS\_PAR.FAULTCODE encodings

ATOS\_PAR.FAULTCODE has the following values:

| Type   | Meaning           | Notes                                                                                                                                                                                                                                                                                                                                                        |
|--------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0xFF   | INV_REQ           | Malformed ATOS request                                                                                                                                                                                                                                                                                                                                       |
| 0xFE   | INV_STAGE         | Request for stage of translation that is not present                                                                                                                                                                                                                                                                                                         |
| 0xFD   | INTERNAL_ERR      | Translation was terminated for miscellaneous reason.                                                                                                                                                                                                                                                                                                         |
| 0x02   | C_BAD_STREAMID    | ATOS_SID.STREAMID out of range of configured Stream table. Note: ATOS_SID.STREAMID might not store bits above the implemented StreamID size. An implementation is permitted but not required to record this error if ATOS_SID.STREAMID is greater than the implemented StreamID size, or might truncate STREAMID to the implemented StreamID size.           |
| 0x03   | F_STE_FETCH       | External abort or error on STE fetch                                                                                                                                                                                                                                                                                                                         |
| 0x04   | C_BAD_STE         | Selected STE invalid or illegal                                                                                                                                                                                                                                                                                                                              |
| 0x06   | F_STREAM_DISABLED | Non-substream request was made (ATOS_SID.SSID_VALID == 0) on configuration with Config[0] == 1 and STE.S1CDMax > 0 and STE.S1DSS == 0b00 , or a request with SubstreamID 0 was made on configuration with Config[0] == 1 and STE.S1CDMax > 0 and STE.S1DSS == 0b10 .                                                                                         |
| 0x08   | C_BAD_SUBSTREAMID | ATOS_SID.SSID out of range of configured CD table. Note: ATOS_SID.SUBSTREAMID might not store bits above the implemented SubstreamID size. An implementation is permitted but not required to record this error if ATOS_SID.SUBSTREAMID is greater than the implemented SubstreamID size, or might truncate SUBSTREAMID to the implemented SubstreamID size. |
| 0x09   | F_CD_FETCH        | External abort or error on CD fetch For a VATOS (or other stage 1-only) request, this is returned where the CD fetch caused a stage 2 fault.                                                                                                                                                                                                                 |
| 0x0A   | C_BAD_CD          | Selected CD invalid or illegal                                                                                                                                                                                                                                                                                                                               |

| Type   | Meaning        | Notes                                                                                                                                                          |
|--------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x0B   | F_WALK_EABT    | External abort or error on translation table walk For a VATOS (or other stage 1-only) request, this is returned where the stage 1 walk caused a stage 2 fault. |
| 0x10   | F_TRANSLATION  | Translation fault                                                                                                                                              |
| 0x11   | F_ADDR_SIZE    | Address Size fault                                                                                                                                             |
| 0x12   | F_ACCESS       | Access flag fault                                                                                                                                              |
| 0x13   | F_PERMISSION   | Permission fault                                                                                                                                               |
| 0x20   | F_TLB_CONFLICT | Translation caused TLB conflict condition                                                                                                                      |
| 0x21   | F_CFG_CONLICT  | Translation caused configuration cache conflict condition                                                                                                      |
| 0x25   | F_VMS_FETCH    | External abort or error on VMS fetch                                                                                                                           |

All other values are Reserved.

The priority order of the C\_* and F\_* errors and faults follow the same order that is set out for Event queue events in 7.3.22 Event queue record priorities , with the relative priorities for INV\_REQ and INV\_STAGE as shown here:

## 1. INV\_REQ

- a. Note: Whether INV\_REQ is to be reported is determined statically before access of configuration structures.
2. INV\_STAGE (point A, see below)
3. C\_BAD\_STREAMID
4. F\_STE\_FETCH
5. C\_BAD\_STE
6. F\_VMS\_FETCH
- a. Note: Relative priority of F\_VMS\_FETCH is defined below.
7. INV\_STAGE (point B, see below)
8. C\_BAD\_SUBSTREAMID
9. F\_STREAM\_DISABLED
10. Translation faults (stage 2, for fetch of a CD)
11. F\_CD\_FETCH
12. C\_BAD\_CD
13. Translation-related faults (stage 1 or stage 2, for input address)

INV\_STAGE is reported after the STE is fetched and valid, at point B, after C\_BAD\_STREAMID, F\_STE\_FETCH and C\_BAD\_STE are checked, if the enabled set of stages of the STE are determined to be incompatible with the request. INV\_STAGE takes precedence over C\_BAD\_SUBSTREAMID, F\_STREAM\_DISABLED, F\_CD\_FETCH, C\_BAD\_CD and all Translation-related faults.

When SMMU\_S\_IDR1.SEL2 == 0 and a Secure ATOS request is made with SMMU\_S\_GATOS\_SID.SSEC == 1, then INV\_STAGE is permitted to be determined statically at point A prior to checking for C\_BAD\_STREAMID.

Note: This is because a Secure stream cannot have stage 2 enabled when SMMU\_S\_IDR1.SEL2 == 0, so an ATOS request for stage 2 information from a Secure stream is always invalid. When SMMU\_S\_IDR1.SEL2 == 1, Secure stage 2 is supported which means that this check cannot be performed statically and must take the STE configuration into consideration at point B, in the same way as for a Non-secure stream.

F\_VMS\_FETCH is reported after C\_BAD\_STE, but its priority relative to other events is IMPLEMENTATION DEFINED.

## 9.1.6 SMMU\_(S\_)VATOS\_SEL

The VATOS interface provides a mechanism to limit the scope of VATOS requests so that VATOS responses only provide information relating to the VMID of the Virtual Machine that is associated with that interface.

Note: Arm expects the VATOS interface to be exposed to one virtual machine at a time.

Note: Arm expects the VATOS interface to be used in scenarios where a Virtual Machine is able to make queries using a physical StreamID number and where a system-specific mechanism describes the presence of the VATOS page in the Virtual Machine address space.

The scope of a VATOS interface is limited to STEs configured to tag translations with a VMID that matches the corresponding SMMU\_(S\_)VATOS\_SEL.VMID field. If the values match, a VATOS request is permitted to return information using that STE. If the values do not match, or the STE does not contain a VMID, a request is denied with C\_BAD\_STE.

A request made through a VATOS interface is checked using this procedure:

1. The VATOS\_ADDR.TYPE of the request is checked, leading to INV\_REQ if it is invalid for a VATOS interface. See section 9.1.3 ATOS\_ADDR .
2. The STE is fetched for the StreamID requested using SMMU\_(S\_)VATOS\_SID. This process might lead to C\_BAD\_STREAMID, F\_STE\_FETCH or C\_BAD\_STE.
3. In some STE configurations, translations are not tagged with a VMID. This is described in the definition of STE.S2VMID. In this case, the result is C\_BAD\_STE.
4. If the configuration of the STE means that translations are tagged with a VMID, the effective STE.S2VMID value is compared against the corresponding SMMU\_(S\_)VATOS\_SEL.VMID value. If the values do not match, the result is C\_BAD\_STE.
5. If the values match, the V ATOS request is permitted to return StreamID-specific information. If the STE configuration is not appropriate for the request, the result is INV\_STAGE.

Note: For example, an STE with stage 2-only translation cannot be queried using VATOS.

6. Any other ATOS response is now possible, for example a fault or error with lower priority than C\_BAD\_STE, or a successful result.

Note: For a Non-secure STE with an effective NS-EL1 StreamWorld, the STE.S2VMID field is used even when stage 1-only translation is used. For a Secure STE with an effective Secure StreamWorld and stage 1-only translation, an effective value of 0 is used for VMID tagging and STE.S2VMID is IGNORED.