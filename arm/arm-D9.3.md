## D9.3 Granular Data Isolation

RKWXTL

All statements in this section require implementation of FEAT\_RME\_GDI.

ICPKHY

The Granular Data Isolation feature enables memory isolation of non-PE data flows from the PEs, within an RME system.

IKCSQM

Two PA spaces are defined for non-PE data granules:

- Non-secure Protected (NSP) memory, which is managed by a PE, using the SMMU, on behalf of a NS device in protected mode.

- System Agent (SA) memory, which is fully isolated from the PEs, and any additional memory management is independent from the PEs.

Note

NSP memory is intended for media pipelines, with flexible NS software management and strong data confidentiality. SA memory is intended for use by higher security on-chip sub-systems that require memory allocation on request.

ICQKLR

NSE2 extends NS and NSE for the addressing of PA spaces:

|   NSE2 |   NSE |   NS | Target PA Space    |
|--------|-------|------|--------------------|
|      0 |     0 |    0 | S - Secure         |
|      0 |     0 |    1 | NS - Non-secure    |
|      0 |     1 |    0 | RT - Root          |
|      0 |     1 |    1 | RL - Realm         |
|      1 |     0 |    0 | SA - System Agent  |
|      1 |     0 |    1 | NSP - NS Protected |
|      1 |     1 |    0 | NA6 - Reserved     |
|      1 |     1 |    1 | NA7 - Reserved     |

RMXHVD

In a PE with FEAT\_RME\_GDI, with the exception of DC CIPAPA , DC CIGDPAPA , DC CIPAE and DC CIGDPAE , NSE2 has the effective value of zero within a PE.

RQCLPT

APEis not permitted to access memory within the NSP or the SA PA spaces, from any Security state.

IQGYGB

Data within the NSP or the SA PA spaces is not anticipated to require PE managed coherency, through the use of cache maintenance operations to the PoC. However, cache maintenance operations to the PoPA are supported.

ICWGLY

FEAT\_RME\_GDI does not define new Security states.