## D21.2 PARTID spaces

RFMXKY

The following physical PARTID spaces are supported:

- Non-secure PARTID space.

- If Secure state is implemented, Secure PARTID space.

- If RME is implemented, both of:

- Realm PARTID space.

- Root PARTID space.

IDTHSD

In an MPAM PE, MPAMIDR\_EL1.SP4 reports whether the MPAM PE supports two or four PARTID spaces.

RDJRPQ

In an MPAM PE without FEAT\_RME, the physical PARTID space sent as part of an MPAM information bundle depends on the Security state and Exception level of the execution producing the request. If the MPAM version implemented is v0p1, the physical PARTID space also depends on the state of the Force Non-secure PARTID space control, MPAM3\_EL3.FORCE\_NS:

## Table D21-5 PARTID space sent by an MPAM PE without FEAT\_RME

| Security state   | PARTID space sent for a request produced by execution at:   | PARTID space sent for a request produced by execution at:   | PARTID space sent for a request produced by execution at:   | In MPAM version v0p1, PARTID space sent when MPAM3_EL3.FORCE_NS is 1:   |
|------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------------|
|                  | EL3                                                         | EL2                                                         | EL1 and EL0                                                 |                                                                         |
| Non-secure state | -                                                           | Non-secure physical PARTID space                            | Non-secure physical PARTID space                            | No change to the behavior a                                             |
| Secure state     | Secure physical PARTID space                                | Secure physical PARTID space                                | Secure physical PARTID space                                | Non-secure physical PARTID space                                        |

In an MPAM PE with FEAT\_RME, the physical PARTID space sent as part of an MPAM information bundle depends on the Security state and Exception level of the execution producing the request, and the state of the alternative PARTID space controls, that select whether a primary or alternative PARTID space is sent:

## Table D21-6 PARTID space sent by an MPAM PE with FEAT\_RME

| Security state    | If primary selected, the primary PARTID space sent for a request produced by execution at:   | If primary selected, the primary PARTID space sent for a request produced by execution at:   | If primary selected, the primary PARTID space sent for a request produced by execution at:   | If alternative selected, the alternative sent:          |
|-------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------|
| Security state    | EL3                                                                                          | EL2                                                                                          | EL1 and EL0                                                                                  | If alternative selected, the alternative sent:          |
| Non- secure state | -                                                                                            | Non-secure physical PARTID space                                                             | Non-secure physical PARTID space                                                             | No change to the behavior a                             |
| Secure state      | -                                                                                            | Secure physical PARTID space                                                                 | Secure physical PARTID space                                                                 | Non-secure physical PARTID space                        |
| Realm state       | -                                                                                            | Realm physical PARTID space                                                                  | Realm physical PARTID space                                                                  | Non-secure physical PARTID space                        |
| Root state        | Root physical PARTID space                                                                   | -                                                                                            | -                                                                                            | Selectable Secure or Non-secure physical PARTID space a |

The Secure physical PARTID space is not used in systems, or system components, that do not implement Secure state.

See also:

RNTMXM

RFFRDD

IVNRRQ

- For detail on how an MPAM PE Requester sends a PARTID space, Encoding PARTID spaces onto PARTID space signals.
- For detail on the alternate PARTID space controls, In an MPAM PE with FEAT\_RME, selection of primary or alternative PARTID space.

## D21.2.1 PARTID space virtualization

ICCVLY

In an MPAM PE, if EL2 is implemented and enabled in the current Security state, and MPAMIDR\_EL1.HAS\_HCR indicates that the MPAM virtualization option is implemented, execution at EL0 and EL1 might produce a virtual PARTID space , that is translated to a physical P ARTID space . For details, see PARTID virtualization.

## D21.2.2 In an MPAM PE with FEAT\_RME, selection of primary or alternative PARTID space

RSWNPB

For EL3 Root state execution:

- MPAM3\_EL3.ALTSP\_EL3 selects whether EL3 produces the primary or alternative PARTID space.
- MPAM3\_EL3.RT\_ALTSP\_NS selects whether the alternative PARTID space is Secure or Non-secure:

## Table D21-7 PARTID space that EL3 produces, in an MPAM PE with FEAT\_RME

|   ALTSP_EL3 | RT_ALTSP_NS   | PARTID space that EL3 produces                              |
|-------------|---------------|-------------------------------------------------------------|
|           0 | X             | Primary PARTID space. Root physical PARTID space.           |
|           1 | 0             | Alternative PARTID space. Secure physical PARTID space.     |
|           1 | 1             | Alternative PARTID space. Non-secure physical PARTID space. |

RDFMYN

For execution below EL3, EL3 is either:

- Forcing primary or alternative PARTID spaces for execution at EL2, EL1, and EL0.
- Permitting EL2 to control its own PARTID space, and the PARTID space for EL1 and EL0.

Forcing primary or alternative PARTID spaces for execution at EL2, EL1, and EL0, is by:

1. MPAM3\_EL3.ALTSP\_HEN=0 disabling the EL2 alternative P ARTID space controls .
2. MPAM3\_EL3.ALTSP\_HFC selecting the primary or alternative PARTID space for execution at EL2, EL1, and EL0.

Permitting EL2 to control its own PARTID space, and the PARTID space for EL1 and EL0, is by:

- MPAM3\_EL3.ALTSP\_HEN=1 enabling the EL2 alternative PARTID space controls, which means that:
- -EL2 can configure MPAM2\_EL2.ALTSP\_EL2 to select the primary or alternative PARTID space for EL2.
- -EL2 can configure MPAM2\_EL2.ALTSP\_HFC to select the primary or alternative PARTID space for EL1 and EL0.

See the following tables for execution at EL2, and at EL1 and EL0, respectively:

## Table D21-8 PARTID space that EL2 produces, when EL2 is enabled in the Security state, in an MPAM PE with FEAT\_RME

|   MPAM3_EL3.ALTSP_HEN | MPAM3_EL3.ALTSP_HFC   | MPAM2_EL2.ALTSP_EL2   | PARTID space that EL2 produces                 |
|-----------------------|-----------------------|-----------------------|------------------------------------------------|
|                     0 | 0                     | X                     | Primary.                                       |
|                     0 | 1                     | X                     | Alternative. Non-secure physical PARTID space. |
|                     1 | X                     | 0                     | Primary.                                       |

|   MPAM3_EL3.ALTSP_HEN | MPAM3_EL3.ALTSP_HFC   |   MPAM2_EL2.ALTSP_EL2 | PARTID space that EL2 produces                 |
|-----------------------|-----------------------|-----------------------|------------------------------------------------|
|                     1 | X                     |                     1 | Alternative. Non-secure physical PARTID space. |

## Table D21-9 PARTID space that EL1 and EL0 produce, in an MPAM PE with FEAT\_RME

|   MPAM3_EL3.ALTSP_HEN | MPAM3_EL3.ALTSP_HFC   | MPAM2_EL2.ALTSP_HFC   | PARTID space that EL1 and EL0 produce          |
|-----------------------|-----------------------|-----------------------|------------------------------------------------|
|                     0 | 0                     | X                     | Primary.                                       |
|                     0 | 1                     | X                     | Alternative. Non-secure physical PARTID space. |
|                     1 | X                     | 0                     | Primary.                                       |
|                     1 | X                     | 1                     | Alternative. Non-secure physical PARTID space. |

RKXKGR

When EL2 is disabled in the current Security state, EL1 and EL0 produce the alternative PARTID space when MPAM3\_EL3.{ALTSP\_HEN, ALTSP\_HFC} are {0, 1}, and produce the primary PARTID space otherwise.

RBTVYC

IHDJCV

When MPAM3\_EL3.MPAMEN is 0, so that MPAM is disabled from EL3, MPAM2\_EL2.{ALTSP\_HFC, ALTSP\_EL2} are treated as {0, 0}, and MPAM3\_EL3.{ALTSP\_HEN, ALTSP\_HFC, ALTSP\_EL3, RT\_ALTSP\_NS} are effective.

MPAMn\_ELx.ALTSP\_FRCD reports whether execution at ELn is being forced to produce the alternative PARTID space:

- MPAM2\_EL2.ALTSP\_FRCD reports, in all implemented Security states, whether EL3 is forcing the alternative PARTID space for execution at EL2.
- MPAM1\_EL1.ALTSP\_FRCD reports, in all implemented Security states, whether EL3 or EL2 is forcing the alternative PARTID space for execution at EL1 and EL0.

There is no ALTSP\_FRCD field in MPAM0\_EL1. There is no mechanism for EL0 to discover whether it is producing the primary or alternative PARTID space. However, EL0 is always producing the same PARTID space as either:

- EL2, when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.
- EL1 otherwise.

## D21.2.3 Encoding PARTID spaces onto PARTID space signals

RVKVCD

The physical PARTID space that an MPAM PE Requester sends as part of an MPAM information bundle is sent by encoding it onto:

- An MPAM\_NS signal if the MPAM PE does not implement RME.
- An MPAM\_SP signal if the MPAM PE implements RME.

Table D21-10 Encoding of the physical PARTID space sent if the MPAM PE does not implement FEAT\_RME

| PARTID space the MPAM PE Requester is sending   | Encoding on MPAM_NS signal   |
|-------------------------------------------------|------------------------------|
| Secure physical PARTID space                    | 0b0                          |
| Non-secure physical PARTID space                | 0b1                          |

Table D21-11 Encoding of the physical PARTID space sent if the MPAM PE implements FEAT\_RME

| PARTID space the MPAM PE Requester is sending   | Encoding on MPAM_SP signal   |
|-------------------------------------------------|------------------------------|
| Secure physical PARTID space                    | 0b00                         |
| Non-secure physical PARTID space                | 0b01                         |
| Root physical PARTID space                      | 0b10                         |
| Realm physical PARTID space                     | 0b11                         |

In MPAM PEs without Secure state, MPAM\_NS encoding 0b0 or MPAM\_SP encoding 0b00 is reserved.

IMRBXT

ITWGKV

INZPRL

SoCs can be constructed comprising Requester components that all support MPAM\_NS, that all support MPAM\_SP, or comprising some that support MPAM\_NS and some that support MPAM\_SP.

In MPAMv0p1, if MPAM3\_EL3.FORCE\_NS is implemented as:

- RAO/WI, Secure PARTIDs are not implemented, and the MPAM PE Requester always sends MPAM\_NS as 1 for both the Secure physical PARTID space and Non-secure Physical PARTID space.
- RW, then setting MPAM3\_EL3.FORCE\_NS to 1 causes the MPAM PE Requester to always send MPAM\_NS as 1 for both the Secure physical PARTID space and Non-secure Physical PARTID space.

See Effect of the MPAM3\_EL3.{SDEFLT, FORCE\_NS} controls on MPAM PE Secure state execution.

## See also:

- PARTID spaces, for detail on how an MPAM PE Requester determines which physical PARTID space to send.