## 12.6 Recommendations for reporting of SMMU events in RAS registers

This section is only a recommendation and is not normative. The RAS System Architecture [2] is the authoritative source.

## 12.6.1 SMMU architectural events

In all of the below, the following approach is used:

- Reporting of the MV field is not captured here.
- Setting the OF field should be performed according to the rules in the RAS System Architecture [2].
- All the error record values in this chapter are captured as though there were no prior errors reported in the error record register. Irrelevant fields are described as 'N/A' for 'not applicable'.
- Implementations must follow the rules in the RAS System Architecture [2] around reporting multiple errors in the same record register.
- None of the errors listed here should be critical, so CI == 0 or unchanged in all the below.

## 12.6.1.1 Deferred error on structure fetch

RAS event: SMMU receives a Deferred error (for example, a poisoned read response) on configuration structure or translation table fetch, leading to F\_WALK\_EABT, F\_STE\_FETCH, F\_CD\_FETCH, F\_VMS\_FETCH.

Signaled to requester as: CA for PCIe requests. Equivalent 'Abort' on other protocols. Note: The RAS architecture permits a mechanism where the value of ERR&lt;n&gt;CTRL.{UE,RUE,WUE} might suppress signaling of External Aborts. Suppressing these External Aborts is not permitted for the SMMU.

Implementation notes: Some SMMUs or memory systems may not support Deferred errors (poison) and therefore cannot detect and report this error.

Reported in RAS error record as:

| ERR<n>STATUS field   | Notes                                                                                 |
|----------------------|---------------------------------------------------------------------------------------|
| AV == 1              | If the physical address details for the error are reported in ERR<n>ADDR.             |
| AV == 0              | If ERR<n>ADDR is RES0 or not updated.                                                 |
| V == 1               | The record is valid.                                                                  |
| UE == 1              | There was an Uncorrected error.                                                       |
| ER == 1              | The SMMUis required to signal the error to the requester as an abort, or CA for PCIe. |
| PN == 1              | The SMMUobserved the Deferred error.                                                  |
| UET == 0b11          | The SMMUSignaled the error to the client and it is Recoverable.                       |
| SERR == 21           | The SMMUcannot further defer the error.                                               |
| DE, CE, OF, CI       | N/A                                                                                   |

## 12.6.1.2 Uncorrectable error on structure fetch

RAS event: SMMU detects Uncorrectable (i.e. not Deferred) error on configuration structure or translation table fetch, leading to F\_WALK\_EABT, F\_STE\_FETCH, F\_CD\_FETCH, F\_VMS\_FETCH.

Implementation notes: Some SMMUs may not be able to distinguish a regular External Abort from a RAS error and therefore cannot detect and report this error.

Signaled to requester as: CA for PCIe requests. Equivalent 'Abort' on other protocols. Note: The RAS architecture permits a mechanism where the value of ERR&lt;n&gt;CTRL.{UE,RUE,WUE} might suppress signaling of External Aborts. Suppressing these External Aborts is not permitted for the SMMU.

Reported in RAS error record as:

| ERR<n>STATUS field   | Notes                                                                                 |
|----------------------|---------------------------------------------------------------------------------------|
| AV == 1              | If the physical address details for the error are reported in ERR<n>ADDR.             |
| AV == 0              | If ERR<n>ADDR is RES0 or not updated.                                                 |
| V == 1               | The record is valid.                                                                  |
| UE == 1              | There was an Uncorrected error.                                                       |
| ER == 1              | The SMMUis required to signal the error to the requester as an abort, or CA for PCIe. |
| PN == 0              | The SMMUdid not observe any poison.                                                   |
| UET == 0b11          | The SMMUSignaled the error to the client and it is Recoverable.                       |
| SERR == 12           | The error was on data from memory.                                                    |
| DE, CE, OF, CI       | N/A                                                                                   |

## 12.6.1.3 Error on Command queue fetch

RAS event: SMMU experiences a RAS error on a CMDQ fetch, leading to SMMU\_(*\_)GERROR.CMDQ\_ERR with CERROR\_ABT reported in SMMU\_(*\_)CMDQ\_CONS.ERR.

Implementation notes: Some SMMUs may not be able to distinguish a regular External Abort from a RAS error and therefore cannot detect and report this error.

Reported in RAS error record as:

| ERR<n>STATUS field   | Notes                                                                     |
|----------------------|---------------------------------------------------------------------------|
| AV == 1              | If the physical address details for the error are reported in ERR<n>ADDR. |
| AV == 0              | If ERR<n>ADDR is RES0 or not updated.                                     |
| V == 1               | The record is valid.                                                      |
| UE == 1              | There was an Uncorrected error.                                           |
| ER == 0              | The error was not signaled as an External Abort by the SMMU.              |
| PN == 0 or 1         | Depending on whether the SMMUsaw corrupt data vs poisoned response.       |
| UET == 0b11          | The SMMUSignaled the error to the client and it is Recoverable.           |
| SERR IN {12, 21}     | 12 corrupted data, 21 for poisoned data.                                  |
| DE, CE, OF, CI       | N/A                                                                       |

## 12.6.2 Common SMMU microarchitectural events

## 12.6.2.1 ECC or EDC error on TLB or configuration cache

RAS event: SMMU needs to use a TLB or Configuration Cache entry but detects that it has been corrupted. This is a Latent error as it does not need to be consumed. In the case of an ECC error, the SMMU corrects the entry. In the case of an EDC error, the SMMU invalidates the entry and performs a fresh configuration fetch or translation table walk.

Implementation notes: Some SMMUs may not have ECC or EDC on TLBs or configuration caches and therefore could never detect this error.

Reported in RAS error record as:

| ERR<n>STATUS field      | Notes                                                 |
|-------------------------|-------------------------------------------------------|
| AV == 0                 | The entry is not associated with an address any more. |
| V == 1                  | The record is valid.                                  |
| ER == 0                 | No error to signal.                                   |
| CE != 0b00              | The error was corrected.                              |
| SERR IN {1, 6, 7, 8, 9} | As appropriate.                                       |
| UE, DE, OF, UET, CI, PN | N/A                                                   |

## 12.6.2.2 Error on data payload of a client transaction

RAS event: SMMU observes corruption on the data payload of a transaction

Implementation notes: Some SMMUs may not have visibility of the data payload at all and therefore cannot detect this error. Even if an SMMU can detect this error, it is IMPLEMENTATION DEFINED whether it reports it. Some SMMUs or memory systems may not support poison. An example range of implementation styles is listed in the second table below.

Reported in RAS error record as:

| ERR<n>STATUS field   | Notes                                                                     |
|----------------------|---------------------------------------------------------------------------|
| AV == 1              | If the physical address details for the error are reported in ERR<n>ADDR. |
| AV == 0              | If ERR<n>ADDR is RES0 or not updated.                                     |
| V == 1               | The record is valid.                                                      |
| CI == 0              | The error is localized and SMMUcan continue operation.                    |
| CE, OF, CI           | N/A                                                                       |

| Scenario                                   | SMMUaction       | ERR<n>STATUS values                            | SERR       |
|--------------------------------------------|------------------|------------------------------------------------|------------|
| SMMUdoes not observe data path             | None             | Not reported in SMMURAS registers.             | N/A        |
| SMMUignores poison on client transactions  | None             | Not reported in SMMURAS registers.             | N/A        |
| Data is poisoned before it arrives at SMMU | Upgrade to Abort | UE == 1, ER == 1, DE N/A, PN == 1, UET == 0b11 | 10         |
| Data is poisoned before it arrives at SMMU | Propagate poison | UE N/A, ER == 0, DE == 1, PN == 1              | 10, 23, 24 |
| Data corrupted in SMMUdata buffer          | Upgrade to Abort | UE == 1, ER == 1, DE N/A, PN == 0, UET == 0b11 | 2          |
| Data corrupted in SMMUdata buffer          | Propagate poison | UE N/A, ER == 0, DE == 1, PN == 0              | 2          |