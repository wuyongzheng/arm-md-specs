## K5.1 About the recommended external debug interface

See the Note on the first page of this appendix for information about the architectural status of this recommended debug interface.

This specification provides a recommended external debug interface for Armv8 and later architectures to define a standard set of connections for validation environments. Generally, the connection between components, such as between the PE and Trace extension, is not described here, although the table does include the signals for the CTI connection. Table K5-1 shows the signals in the recommended interface.

Table K5-1 Recommended debug interface signals

| Name            | Direction   | Description                                | Notes                                                                                                                                                         |
|-----------------|-------------|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DBGEN           | In          | External debug enable                      | -                                                                                                                                                             |
| SPIDEN          | In          | Secure privileged external debug enable    | -                                                                                                                                                             |
| RLPIDEN         | In          | Realm privileged external debug enable     | Only if FEAT_RME is implemented.                                                                                                                              |
| RTPIDEN         | In          | Root privileged external debug enable      |                                                                                                                                                               |
| NIDEN           | In          | External profiling and trace enable        | If FEAT_Debugv8p4 is implemented, this signal is not implemented.                                                                                             |
| SPNIDEN         | In          | Secure external profiling and trace enable | If FEAT_Debugv8p4 is implemented, this signal is not implemented.                                                                                             |
| EDBGRQ          | In          | External halt request                      | IMPLEMENTATION DEFINED mechanism to halt the PE. See EDBGRQand DBGACK.                                                                                        |
| DBGACK          | Out         | Debug Acknowledge                          | Indicate to the system that a PE is in Debug state. See EDBGRQand DBGACK.                                                                                     |
| COMMIRQ         | Out         | DCCinterrupt                               | Interface to an interrupt controller. See Interrupt-driven use of the DCCand the pseudocode for function CheckForDCCInterrupts() .                            |
| PMUIRQ          | Out         | Performance Monitor overflow               | Interface to an interrupt controller. See Behavior on overflow.                                                                                               |
| COMMRX COMMTX   | Out Out     | DTRRXis full DTRTX is empty                | Provided for legacy connection to an interrupt controller only. See Interrupt-driven use of the DCCand the pseudocode for function CheckForDCCInterrupts () . |
| PMUEVENT[n:0]   | Out         | Performance Monitors event bus             | See PMUEVENTbus.                                                                                                                                              |
| DBGNOPWRDWN     | Out         | Emulate low-power state request            | Interface to a power controller. See Emulating low-power states.                                                                                              |
| DBGPWRUPREQ     | Out         | Core powerup request                       | Interface to a power controller. See Powerup request mechanism.                                                                                               |
|                 |             |                                            | Interface to a power controller.                                                                                                                              |
| DBGRSTREQ       | Out         | Warm reset request                         | See EDPRCR.CWRR.                                                                                                                                              |
| DBGBUSCANCELREQ | Out         | Allow asynchronous entry to Debug state    | Extension to the bus interface. See EDRCR.CBRRQ.                                                                                                              |
| DBGPWRDUP       | In          | Core powerup status                        | Interface to a power controller. See EDPRSR.PU.                                                                                                               |

| Name             | Direction   | Description                                                   | Notes                                                                                                                                       |
|------------------|-------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| DBGROMADDR[n:12] | In          | MDRAR_EL1.ROMADDR                                             | n depends on the size of the physical address space. Arm recommends these signals are tied LOW .                                            |
| DBGROMADDRV      | In          | MDRAR_EL1.Valid                                               | Arm recommends these signals are tied LOW .                                                                                                 |
| PRESETDBG        | In          | External Debug reset                                          | -                                                                                                                                           |
| CPUPORESET       | In          | Cold reset                                                    | -                                                                                                                                           |
| CORERESET        | In          | Warm reset                                                    | -                                                                                                                                           |
| PSELDBG          | In          | Debug APB interface a                                         | For details, see AMBAAPB3 . Arm recommends a single port for all integrated debug components. PADDRDBG31 distinguishes memory-mapped        |
| PENABLEDBG       | In          |                                                               | For details, see AMBAAPB3 . Arm recommends a single port for all integrated debug components. PADDRDBG31 distinguishes memory-mapped        |
| PWRITEDBG        | In          |                                                               | For details, see AMBAAPB3 . Arm recommends a single port for all integrated debug components. PADDRDBG31 distinguishes memory-mapped        |
| PRDATADBG[31:0]  | Out         |                                                               | and Debug Access Port accesses:                                                                                                             |
| PWDATADBG[31:0]  | In          |                                                               | For details, see AMBAAPB3 . Arm recommends a single port for all integrated debug components. PADDRDBG31 distinguishes memory-mapped        |
| PADDRDBG[n:2] b  | In          |                                                               | 0 Memory-mapped access 1 Debug Access Port access                                                                                           |
| PREADYDBG        | Out         |                                                               | If FEAT_Debugv8p4 is implemented,                                                                                                           |
| PSLVERRDBG       | Out         |                                                               | PPROTDBG[1] distinguishes between Secure and Non-secure accesses.                                                                           |
| PCLKDBG          | In          |                                                               | For details, see Non-secure, Secure, Realm,                                                                                                 |
| PCLKENDBG        | In          |                                                               | and Root views of the debug registers.                                                                                                      |
| PPROTDBG[1]      | In          |                                                               | 0 Memory-mapped access 1 Debug Access Port access                                                                                           |
| CTICHIN          | In          | CoreSight channel interface                                   | For details, see the Arm ® CoreSight™ Architecture Specification . TheACK signals are not required if the channel interface is synchronous. |
| CTICHOUTACK      | In          | CoreSight channel interface                                   | For details, see the Arm ® CoreSight™ Architecture Specification . TheACK signals are not required if the channel interface is synchronous. |
| CTICHOUT         | Out         | CoreSight channel interface                                   | For details, see the Arm ® CoreSight™ Architecture Specification . TheACK signals are not required if the channel interface is synchronous. |
| CTICHINACK       | Out         | CoreSight channel interface                                   | For details, see the Arm ® CoreSight™ Architecture Specification . TheACK signals are not required if the channel interface is synchronous. |
| CTIIRQ           | Out         | CTI interrupt, see Description and allocation of CTI triggers | Implements a handshake for an edge-sensitive interrupt.                                                                                     |
| CTIIRQACK        | In          | CTI interrupt, see Description and allocation of CTI triggers | Implements a handshake for an edge-sensitive interrupt.                                                                                     |
| ATDATA[nx8-1:0]  | Out         | AMBA4ATBinterface c                                           | For details, see the AMBA4ATBProtocol Specification, ATBv1.0 and ATBv1.1 . Only available if the OPTIONAL Trace extension is implemented.   |
| ATBYTES[n-1:0]   | Out         | AMBA4ATBinterface c                                           | For details, see the AMBA4ATBProtocol Specification, ATBv1.0 and ATBv1.1 . Only available if the OPTIONAL Trace extension is implemented.   |
| ATID[6:0]        | Out         | AMBA4ATBinterface c                                           | For details, see the AMBA4ATBProtocol Specification, ATBv1.0 and ATBv1.1 . Only available if the OPTIONAL Trace extension is implemented.   |
| ATREADY          | In          | AMBA4ATBinterface c                                           | For details, see the AMBA4ATBProtocol Specification, ATBv1.0 and ATBv1.1 . Only available if the OPTIONAL Trace extension is implemented.   |
| ATVALID          | Out         | AMBA4ATBinterface c                                           | For details, see the AMBA4ATBProtocol Specification, ATBv1.0 and ATBv1.1 . Only available if the OPTIONAL Trace extension is implemented.   |
| AFREADY          | Out         | AMBA4ATBinterface c                                           | For details, see the AMBA4ATBProtocol Specification, ATBv1.0 and ATBv1.1 . Only available if the OPTIONAL Trace extension is implemented.   |
| AFVALID          | Out         | AMBA4ATBinterface c                                           | For details, see the AMBA4ATBProtocol Specification, ATBv1.0 and ATBv1.1 . Only available if the OPTIONAL Trace extension is implemented.   |
| SYNCREQ          | In          | AMBA4ATBinterface c                                           | For details, see the AMBA4ATBProtocol Specification, ATBv1.0 and ATBv1.1 . Only available if the OPTIONAL Trace extension is implemented.   |
| ATCLK            | In          | AMBA4ATBinterface c                                           | For details, see the AMBA4ATBProtocol Specification, ATBv1.0 and ATBv1.1 . Only available if the OPTIONAL Trace extension is implemented.   |
| ATCLKEN          | In          | AMBA4ATBinterface c                                           | For details, see the AMBA4ATBProtocol Specification, ATBv1.0 and ATBv1.1 . Only available if the OPTIONAL Trace extension is implemented.   |
| ATRESET          | In          | AMBA4ATBinterface c                                           | For details, see the AMBA4ATBProtocol Specification, ATBv1.0 and ATBv1.1 . Only available if the OPTIONAL Trace extension is implemented.   |

Figure K5-1 shows the recommended debug interface.

Figure K5-1 Recommended external debug interface, including the APB4 Completer port

<!-- image -->

## K5.1.1 EDBGRQ and DBGACK

EDBGRQ is an IMPLEMENTATION DEFINED means of generating the External Debug Request debug event described in External Debug Request debug event.

The PE asserts DBGACK when the PE is in Debug state. The PE might also include variants of this signal:

## DBGTRIGGER

Asserted by the PE when it commits to entering Debug state.

## DBGCPUDONE

Asserted by the PE when it has completed all Non-debug state memory accesses and Debug state entry is complete. DBGCPUDONE indicates that memory accesses issued by the PE result from operations originating from debugger commands.

In previous architecture versions, these signals provide an interface between the PE and cross-trigger logic. In Armv8, the architectural Cross-Trigger Interface provides this functionality for external debuggers.

## K5.1.2 Non-secure, Secure, Realm, and Root views of the debug registers

If FEAT\_Debugv8p4 is implemented, the external debug interface has views of debug registers for each physical address space, Non-secure, Secure and, if FEAT\_RME is implemented, Realm and Root. The DAP must ensure that accesses are

made only when permitted. The Arm Debug Interface describes a standard APB-AP programmers' model for APB4, with the PPROTDBG[1] and, if FEAT\_RME is implemented, PNSEDBG signals used to determine the physical address space that is accessed. This model is recommended for new designs that do not implement FEAT\_RME, and is required for new designs that implement FEAT\_RME.

If FEAT\_RME is not implemented, FEAT\_Debugv8p4 is implemented, and an APB-AP implements an APB3 Requester port, which does not support Secure and Non-secure views, Arm recommends that the following is implemented:

- If SPIDEN is HIGH and DBGEN is HIGH, all external debug accesses are treated as Secure.
- If either SPIDEN is LOW or DBGEN is LOW, all external debug accesses are treated as Non-secure.

If the PE APB Completer port is APB4, this might be implemented by, for example, fixing PPROTDBG[1] to the inverse of ( SPIDEN &amp; DBGEN ) when bridging from APB3 to APB4.