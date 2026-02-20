## D11.2 The Guarded Control Stack

| G THDMB   | FEAT_GCS allows software to use a separate and protected stack for storing control flow information.                                                                                            |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D KSDTT   | The Guarded Control Stack Pointer Registers, GCSPR_ELx, are GCSPR_EL0, GCSPR_EL1, GCSPR_EL2, GCSPR_EL3.                                                                                         |
| R WYQWD   | While executing at ELx, the Guarded Control Stack uses GCSPR_ELx as the current Guarded Control Stack pointer register.                                                                         |
| R WCVQY   | All GCSPR_ELx are 64 bits wide and hold a virtual address in the current translation regime.                                                                                                    |
| D DWRNV   | Each entry in the Guarded Control Stack is called a Guarded Control Stack record.                                                                                                               |
| D NKMHW   | AGuarded Control Stack record is one of the following: • AGuarded Control Stack procedure return record. • AGuarded Control Stack exception return record. • AGuarded Control Stack cap record. |
| R KDDMV   | The size of a Guarded Control Stack procedure return record is 8 bytes.                                                                                                                         |
| R VNZWB   | The size of a Guarded Control Stack cap record is 8 bytes.                                                                                                                                      |
| R KYFJK   | The size of a Guarded Control Stack exception return record is 32 bytes.                                                                                                                        |

## D11.2.1 Enabling the Guarded Control Stack

IRNKDG FEAT\_GCS augments existing procedure call and return instructions to additionally push and pop to the Guarded Control Stack.

RBYVYL The Guarded Control Stack at ELx is PCR Selected if GCSCR\_ELx.PCRSEL is 1, where x is 1 or greater.

The Guarded Control Stack at EL0 is PCR Selected if GCSCRE0\_EL1.PCRSEL is 1.

RKJHKJ The Guarded Control Stack at ELx is PCR Enabled if the Guarded Control Stack is PCR Selected and GCS Enabled at ELx.

RWFTRC The Guarded Control Stack at ELx is GCS Enabled if all of the following are true:

- The PE is executing in AArch64 state.
- The Guarded Control Stack at ELx is PCR Selected.
- At EL0 and EL1, any of the following are true:
- -
- EL2 is not implemented or disabled in the current Security state.
- -The Effective value of HCR\_EL2.{E2H,TGE} is {1, 1}.
- -SCR\_EL3.HXEn is 1 and HCRX\_EL2.GCSEn is 1.
- At EL0, EL1, and EL2, any of the following are true:
- -EL3 is not implemented.
- -SCR\_EL3.GCSEn is 1.

The Guarded Control Stack at ELx is GCS Disabled if the Guarded Control Stack is not GCS Enabled at ELx.

RGCVKH