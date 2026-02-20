## D11.6 Stage 2 Permission model

IRXBNM

Unless otherwise stated, for the purpose of permission checking in stage 2 translations and the purposes of granule protection checks performed by FEAT\_RME, Guarded Control Stack data access are considered as explicit data accesses produced by other load/store instructions.

ISWMHZ

While the Effective value of HCR\_EL2.{E2H, TGE} is {0, 1}, stage 1 translation is disabled and stage 2 does not have any special permissions for the Guarded Control Stack at EL0. The architecture provides no additional protection for the EL0 Guarded Control Stack while the PE is executing in this configuration.

## D11.6.1 Hardening Stage 1 translations

DDDFTT

VTCR\_EL2.GCSH provides an mechanism to enforce the use of stage 1 translations that are hardened by FEAT\_THE.