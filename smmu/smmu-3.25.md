## 3.25 Granule Protection Checks

The Realm Management Extension, FEAT\_RME, [2] specifies the behavior of granule protection checks. An SMMUwith RME performs the same checks for non-PE Requesters.

The format and meaning of the GPT is the same in an SMMU with RME as it is in FEAT\_RME.

The invalidation and synchronization mechanisms for updates to the GPT are the same as for FEAT\_RME.

The SMMU configuration registers for the GPT base address and format are equivalent to those in FEAT\_RME.

See also 17.4 Assignment of PARTID and PMG for SMMU-originated transactions .

Granule protection checks are enabled only when SMMU\_ROOT\_CR0.GPCEN is 1. All statements in this section that describe how granule protection checks are performed only apply when granule protection checks are enabled.

## 3.25.1 Client-originated accesses

Accesses to all physical addresses, except for fetches of GPT information, are subject to granule protection checks.

A client-originated access that experiences a GPC fault is signaled to the client device in the same manner as an External abort.

A client-originated access that experiences a GPC fault on the output address of the access is not reported in the Event queue.

## 3.25.1.1 GPC for client devices without a StreamID

Granule protection checks also apply to accesses from client devices that are not associated with a StreamID. These devices are referred to as NoStreamID devices.

NoStreamID devices only access PA space, and are not associated with any stage 1 or stage 2 translation configuration.

The GPC fault reporting behavior for accesses from NoStreamID devices is the same as for regular client-originated accesses.

NoStreamID devices are not associated with a SEC\_SID value.

Transactions issued by a NoStreamID device include both a physical address and a PA space.

An access from a NoStreamID device with a physical address that exceeds the implemented output address size, advertised in SMMU\_IDR5.OAS, is terminated with an abort and no Event record or fault is recorded.

The SMMU does not perform any architectural transformations or overrides on NoStreamID accesses, but the SMMUmay apply protocol-specific normalization on transaction attributes.

## 3.25.1.2 Speculative and hint accesses

Note: The SMMU does not report faults encountered during a speculative translation request, translation of transactions marked as speculative, prefetch commands, or for NW-DCP or DH transactions. See also 3.14 Speculative accesses .

For an SMMU with RME, GPC faults encountered during a speculative translation request, translation of transactions marked as speculative, prefetch commands, or for NW-DCP or DH transactions, are reported as follows:

- No event record is generated.
- If SMMU\_IDR0.RME\_IMPL = 0, it is CONSTRAINED UNPREDICTABLE whether the GPC fault is reported or not reported. If it is reported, then it is reported in the appropriate SMMU\_ROOT\_GPF\_FAR or SMMU\_ROOT\_GPT\_CFG\_FAR register, if that register does not already contain an active fault.
- If SMMU\_IDR0.RME\_IMPL = 1, the granule protection check fault is not reported.

For speculative translation requests, then:

- If SMMU\_IDR0.RME\_IMPL = 0, it is CONSTRAINED UNPREDICTABLE whether the GPC on the output address of a translation request is applied at the time of the translation or only when a transaction using the translation is issued.
- If SMMU\_IDR0.RME\_IMPL = 1, the GPC on the output address of a translation request is applied at the time of the translation.

## 3.25.2 Interactions with PCIe ATS

Consistent with the rules for all accesses, all PCIe client transactions are subject to granule protection checks.

The SMMU\_CR0.ATSCHK bit has no effect on granule protection checks.

If an SMMU-originated access experiences a GPC fault while servicing an ATS Translation Request, the SMMU responds to the ATS Translation Request as Completer Abort.

If an ATS Translation Request is completed with Success and R == W == 0, the address in the Translation Completion is not valid and it is not subject to granule protection checks.

If SMMU\_IDR0.RME\_IMPL == 1, RME features are supported and the SMMU performs the GPC on the output address for the result of an ATS Translation Request before sending the completion.

The SMMU returns a translation region size in the ATS Translation Completion such that the GPC passes for accesses to anywhere in the region.

If SMMU\_IDR0.RME\_IMPL == 0, the SMMU is permitted but not required to perform a GPC on the output address for the result of an ATS Translation Request.

If the output address for an ATS Translation Request fails a GPC, the SMMU responds to the ATS Translation Request as Completer Abort.

ATS Translated transactions are subject to granule protection checks.

An ATS Translated transaction that fails the GPC is terminated with an abort.

## 3.25.3 SMMU-originated accesses

An SMMU-originated access that experiences a GPC fault is reported as though it had experienced an External abort.

Consistent with the behavior of F\_STE\_FETCH, F\_CD\_FETCH, F\_VMS\_FETCH and F\_WALK\_EABT, signaling and reporting of these failures is not affected by the value of the CD.{A, R, S} bits nor the STE.{S2S, S2R} bits.

For an SMMU with SMMU\_IDR0.RME\_IMPL == 1:

- For each of the F\_STE\_FETCH, F\_CD\_FETCH, F\_VMS\_FETCH and F\_WALK\_EABT event records, there is a new field at bit 80 named GPCF.
- An F\_STE\_FETCH, F\_CD\_FETCH, F\_VMS\_FETCH or F\_WALK\_EABT arising from a GPC fault is reported with GPCF=1.
- An F\_STE\_FETCH, F\_CD\_FETCH, F\_VMS\_FETCH or F\_WALK\_EABT arising for a reason other than a GPC fault is reported with GPCF=0. This is unchanged from an SMMU without SMMU\_IDR0.RME\_IMPL == 1.

For example, if the SMMU experiences a GPC fault on an access to an STE, it is reported as F\_STE\_FETCH, with GPCF=1. This is signaled to the client as an External abort.

For example, if the SMMU experiences a GPC fault on an access to the Non-secure Event queue, it is reported through SMMU\_GERROR.EVENTQ\_ABT\_ERR.

## 3.25.4 Reporting of GPC faults

The reasons for a GPC fault are categorized into three groups:

- Faults arising from an access to a Location forbidden by the GPT configuration, referred to as a Granule Protection Fault (GPF).
- Faults arising from misconfiguration of SMMU\_ROOT\_GPT\_BASE, SMMU\_ROOT\_GPT\_BASE\_CFG or the GPT, referred to as a GPT lookup error .
- Faults arising from RAS errors.

The following error conditions represent a GPF, and are reported in SMMU\_ROOT\_GPF\_FAR:

- An access to a PA space other than Non-secure has a physical address that exceeds the range configured in SMMU\_ROOT\_GPT\_BASE\_CFG.PPS.
- An access was attempted to a location that is forbidden by the configuration in the GPT.

The following error conditions represent a GPT lookup error, and are reported in SMMU\_ROOT\_GPT\_CFG\_FAR:

- Fields in SMMU\_ROOT\_GPT\_BASE\_CFG are configured to reserved values.
- Configuration of SMMU\_ROOT\_GPT\_BASE\_CFG.PPS to exceed SMMU\_IDR5.OAS.
- Configuration of SMMU\_ROOT\_GPT\_BASE\_CFG.{SH, IRGN, ORGN} to an invalid combination.
- SMMU\_ROOT\_GPT\_BASE.ADDR is configured to exceed the size configured in SMMU\_ROOT\_GPT\_BASE\_CFG.PPS.
- The output address of a GPT Table Entry exceeds the size configured in SMMU\_ROOT\_GPT\_BASE\_CFG.PPS.
- The SMMU depends on using values in an invalid GPT Entry.
- The SMMU experienced an External abort while fetching a GPT Entry.
- The SMMU experienced a RAS error while fetching a GPT Entry. This is reported in the same manner as if the SMMU experienced an External abort while fetching a GPT Entry.

## 3.25.5 SMMU behavior if a GPC fault is active

If a client-originated or SMMU-originated access experiences a GPF reported in SMMU\_ROOT\_GPF\_FAR, then:

- If there is no prior GPF in SMMU\_ROOT\_GPF\_FAR, the appropriate syndrome information is recorded in SMMU\_ROOT\_GPF\_FAR.
- Other accesses that do not experience a GPF or GPT lookup error continue as specified.
- The GPF remains active until software writes 0 to SMMU\_ROOT\_GPF\_FAR.FAULT.

If a client-originated or SMMU-originated access experiences a GPT lookup error reported in SMMU\_ROOT\_GPT\_CFG\_FAR, then:

- If there is no prior GPT lookup error in SMMU\_ROOT\_GPT\_CFG\_FAR, the appropriate syndrome information is recorded in SMMU\_ROOT\_GPT\_CFG\_FAR.
- Other accesses that do not experience a GPF or GPT lookup error continue as specified.
- The GPT lookup error remains active until software writes 0 to SMMU\_ROOT\_GPT\_CFG\_FAR.FAULT.

An SMMU with RME has two additional edge-triggered wired interrupts:

| Source      | Trigger reason                                    |
|-------------|---------------------------------------------------|
| GPF_FAR     | An error becomes active in SMMU_ROOT_GPF_FAR.     |
| GPT_CFG_FAR | An error becomes active in SMMU_ROOT_GPT_CFG_FAR. |

## 3.25.6 Observability of GPC faults

If the termination of a client transaction as a result of a GPC fault is observable to the client device, then:

- If the appropriate SMMU\_ROOT\_GPF\_FAR or SMMU\_ROOT\_GPT\_CFG\_FAR register already contained an active fault, then it is not updated in this case.
- If the appropriate SMMU\_ROOT\_GPF\_FAR or SMMU\_ROOT\_GPT\_CFG\_FAR register did not already contain an active fault, then the related syndrome information is observable in the appropriate register.

If an interrupt indicating the presence of a GPC fault is observable, then the syndrome information is observable in the SMMU\_ROOT\_GPF\_FAR or SMMU\_ROOT\_GPT\_CFG\_FAR register as appropriate.

If the termination of a client transaction as a result of a GPC fault has been observable to the client device, completion of a subsequent CMD\_SYNC guarantees observability of any related events in the Event queue or, if the Event queue is unwritable, that the Event will not become observable.

For an SMMU with SMMU\_ROOT\_IDR0.BGPTM == 1, then:

- After completion of a broadcast TLBI *PA* and DSB instruction on the PE, completion of a subsequent CMD\_SYNC guarantees that no Events relating to GPT configuration invalidated by that TLBI and DSB will later be made observable in the Event queue.
- After a broadcast TLBI *PA* instruction on the PE, completion of a subsequent DSB instruction guarantees that any errors reported in the SMMU\_ROOT\_GPF\_FAR or SMMU\_ROOT\_GPT\_CFG\_FAR registers relating to GPT configuration invalidated by that TLBI are already observable.

For an SMMU with SMMU\_ROOT\_IDR0.RGPTM == 1, then:

- After completion of a register-based TLBI by PA, indicated by SMMU\_ROOT\_TLBI\_CTRL.RUN, completion of a subsequent CMD\_SYNC guarantees that no Events relating to GPT configuration invalidated by that TLBI by PA will later be made observable in the Event queue.
- Completion of a register-based TLBI by PA, indicated by SMMU\_ROOT\_TLBI\_CTRL.RUN, guarantees that any errors reported in the SMMU\_ROOT\_GPF\_FAR or SMMU\_ROOT\_GPT\_CFG\_FAR registers relating to GPT configuration invalidated by that TLBI by PA are already observable.

If an F\_STE\_FETCH, F\_CD\_FETCH, F\_VMS\_FETCH or F\_WALK\_EABT with GPCF == 1 is observable in the Event queue then either:

- If the appropriate SMMU\_ROOT\_GPF\_FAR or SMMU\_ROOT\_GPT\_CFG\_FAR register already contained an active fault, then it is not updated in this case.
- If the appropriate SMMU\_ROOT\_GPF\_FAR or SMMU\_ROOT\_GPT\_CFG\_FAR register did not already contain an active fault, then the related syndrome information is observable in the appropriate register.

If an update to SMMU\_(*\_)GERROR resulting from a GPC fault is observable, then either:

- If the appropriate SMMU\_ROOT\_GPF\_FAR or SMMU\_ROOT\_GPT\_CFG\_FAR register already contained an active fault, then it is not updated in this case.
- If the appropriate SMMU\_ROOT\_GPF\_FAR or SMMU\_ROOT\_GPT\_CFG\_FAR register did not already contain an active fault, then the related syndrome information is observable in the appropriate register.

If a fault to be reported in SMMU\_(*\_)GERROR is observable in SMMU\_ROOT\_GPF\_FAR or SMMU\_ROOT\_GPT\_CFG\_FAR, then the fault will also be reported in SMMU\_(*\_)GERROR in finite time. The existing mechanisms for ensuring the visibility of errors in SMMU\_(*\_)GERROR also apply in this case. For example, completion of an Update of SMMU\_CR0.EVENTQEN to 0 guarantees observability of any errors to be reported in SMMU\_GERROR.EVENTQ\_ABT\_ERR.