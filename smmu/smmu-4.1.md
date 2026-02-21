## 4.1 Commands overview

## 4.1.1 Command opcodes

All entries in the Command queue are 16 bytes long. All Command queue entries are little-endian. Each command begins with an 8-bit command opcode, defined as follows:

| Command opcode   | Command name                                                               |
|------------------|----------------------------------------------------------------------------|
| 0x00             | Reserved                                                                   |
| 0x01             | CMD_PREFETCH_CONFIG                                                        |
| 0x02             | CMD_PREFETCH_ADDR                                                          |
| 0x03             | CMD_CFGI_STE                                                               |
| 0x04             | CMD_CFGI_STE_RANGE Note: CMD_CFGI_ALL has the same opcode as this command. |
| 0x05             | CMD_CFGI_CD                                                                |
| 0x06             | CMD_CFGI_CD_ALL                                                            |
| 0x07             | CMD_CFGI_VMS_PIDM                                                          |
| 0x08 - 0x0A      | Reserved                                                                   |
| 0x10             | CMD_TLBI_NH_ALL                                                            |
| 0x11             | CMD_TLBI_NH_ASID                                                           |
| 0x12             | CMD_TLBI_NH_VA                                                             |
| 0x13             | CMD_TLBI_NH_VAA                                                            |
| 0x14 - 0x17      | Reserved                                                                   |
| 0x18             | CMD_TLBI_EL3_ALL                                                           |
| 0x19             | Reserved                                                                   |
| 0x1A             | CMD_TLBI_EL3_VA                                                            |
| 0x1B - 0x1F      | Reserved                                                                   |
| 0x20             | CMD_TLBI_EL2_ALL                                                           |
| 0x21             | CMD_TLBI_EL2_ASID                                                          |
| 0x22             | CMD_TLBI_EL2_VA                                                            |
| 0x23             | CMD_TLBI_EL2_VAA                                                           |
| 0x24 - 0x27      | Reserved                                                                   |

## Chapter 4. Commands

- 4.1. Commands overview

| Command opcode   | Command name         |
|------------------|----------------------|
| 0x28             | CMD_TLBI_S12_VMALL   |
| 0x29             | Reserved             |
| 0x2A             | CMD_TLBI_S2_IPA      |
| 0x2B - 0x2F      | Reserved             |
| 0x30             | CMD_TLBI_NSNH_ALL    |
| 0x31 - 0x3F      | Reserved             |
| 0x40             | CMD_ATC_INV          |
| 0x41             | CMD_PRI_RESP         |
| 0x42 - 0x43      | Reserved             |
| 0x44             | CMD_RESUME           |
| 0x45             | CMD_STALL_TERM       |
| 0x46             | CMD_SYNC             |
| 0x47 - 0x4F      | Reserved             |
| 0x50             | CMD_TLBI_S_EL2_ALL   |
| 0x51             | CMD_TLBI_S_EL2_ASID  |
| 0x52             | CMD_TLBI_S_EL2_VA    |
| 0x53             | CMD_TLBI_S_EL2_VAA   |
| 0x54 - 0x57      | Reserved             |
| 0x58             | CMD_TLBI_S_S12_VMALL |
| 0x59             | Reserved             |
| 0x5A             | CMD_TLBI_S_S2_IPA    |
| 0x5B - 0X5F      | Reserved             |
| 0x60             | CMD_TLBI_SNH_ALL     |
| 0x61 - 0x6F      | Reserved             |
| 0x70             | CMD_DPTI_ALL         |
| 0x71 - 0x72      | Reserved             |
| 0x73             | CMD_DPTI_PA          |

| Command opcode   | Command name           |
|------------------|------------------------|
| 0x74 - 0x7F      | Reserved               |
| 0x80 - 0x8F      | IMPLEMENTATION DEFINED |
| 0x90 - 0xFF      | Reserved               |

## 4.1.2 Submitting commands to the Command queue

Commands are submitted to the SMMU by writing them to the Command queue then, after ensuring their visibility to the SMMU, updating the SMMU\_(*\_)CMDQ\_PROD.WR index which notifies the SMMU that there are commands to process. The SMMU does not execute commands beyond the CMDQ\_PROD.WR index and, when commands are able to be processed as described in this chapter, a write to SMMU\_(*\_)CMDQ\_PROD.WR is all that is required from software to cause the SMMU to consider newly-produced commands. See section 3.21.2 Queues .

Commands are able to be processed from the Command queue when all of the following conditions are met:

- The Command queue CONS and PROD indexes indicate that the queue is not empty.
- The Command queue is enabled through SMMU\_(*\_)CR0.CMDQEN.
- No Command queue error is active for the given Command queue.

The SMMU processes commands in a timely manner until all commands are consumed, or a command queue error occurs, or the queue is disabled.

When SMMU\_IDR0.SEV == 1, the SMMU triggers a WFE wake-up event when a Command queue becomes non-full and an agent external to the SMMU could have observed that the queue was previously full. This applies to the Non-secure Command queue and, if implemented, the Secure Command queue.

Note: Arm expects that an attempt to insert a command into the queue will first observe from SMMU\_(*\_)CMDQ\_CONS whether the queue has space, and if it is full might then poll the SMMU\_(*\_)CMDQ\_CONS index in a loop until the queue becomes non-full. Such a loop can be throttled using the WFE instruction when the SMMU and system supports sending of WFE wake-up events.

The behaviors of some commands are dependent on SMMU register state. Register state must not be altered between such a command having been submitted to the Command queue and the command completion. If a register field is changed while a dependent command could be being processed, it is UNPREDICTABLE whether the command is interpreted under the new or old register field value.

## 4.1.3 Command errors

A Command queue CERROR\_ILL error occurs when:

- A Reserved command opcode is encountered.
- A valid command opcode is used with invalid parameters, see the individual command descriptions.
- A valid command opcode is used and a Reserved or undefined field is optionally detected as non-zero, which results in the command being treated as malformed.

Some commands, where specified, are IGNORED in certain circumstances. If a command causes a CERROR\_ILL this takes precedence over whether the command is IGNORED or not.

A command queue CERROR\_ABT error occurs when:

- An external abort is encountered upon accessing memory.

The SMMU stops command consumption immediately upon the first occurrence of an error, so that the SMMU\_(*\_)CMDQ\_CONS.RD index indicates the command that could not be correctly consumed, and the

error code is reported. See section 7.1 Command queue errors for details on Command queue error reporting and recovery.

## 4.1.4 Consumption of commands from the Command queue

A command is Consumed when the value observed in the SMMU\_(*\_)CMDQ\_CONS.RD index register passes beyond the location of the command in the queue. This means that:

- As defined by the normal circular queue semantics, the location has been read by the SMMU and the producer might later re-use the location for a different command.
- Where explicitly noted in a command description, certain side effects or guarantees have occurred.
- -Where not noted, no conclusions can be drawn from the Consumption of a command.

The SMMU\_(*\_)CMDQ\_CONSindex can be polled to determine whether a specific command has been Consumed. See section 4.8 Command Consumption summary for a summary of Consumption behavior.

A CMD\_SYNC command is provided as a mechanism to ensure completion of commands submitted to the same queue at a location before the CMD\_SYNC, including side effects. A CMD\_SYNC is not required to be issued in order to start the processing of earlier commands.

Note: A CMD\_SYNC is used where it is necessary to determine completion of prior commands, such as a TLB invalidation, but commands are able to complete without depending on a CMD\_SYNC.

## 4.1.5 Reserved fields

All non-specified fields in the commands are RES0. An implementation is permitted to check whether these fields are zero. An implementation does one of the following:

- Detects non-zero use of a Reserved field as a malformed command, resulting in CERROR\_ILL.
- Ignores the entirety of any Reserved fields.

Some combinations or ranges of parameter values are defined in this section to be ILLEGAL and use of these values results in a CERROR\_ILL command error.

## 4.1.6 Common command fields

These fields are common to more than one command and have the following behavior:

- SubstreamID and Substream Valid (SSV)
- -SSV indicates whether a SubstreamID is provided.
- 0: SubstreamID not supplied.
- 1: SubstreamID supplied.
- When SMMU\_S\_IDR1.SECURE\_IMPL == 1, SSec is used by commands on the Secure Command queue to indicate whether the given StreamID parameter is Secure or Non-secure, in a similar way to SEC\_SID for an input transaction (see section 3.10.1 StreamID Security state (SEC\_SID) ):
- -Commands on the Non-secure Command queue must set SSec == 0, where present, and cannot affect Secure streams. A command on the Non-secure Command queue with SSec == 1 is ILLEGAL, regardless of whether Secure state is supported, and raises CERROR\_ILL.

|   SSec | Meaning                |
|--------|------------------------|
|      0 | StreamID is Non-secure |
|      1 | StreamID is Secure     |

- -For the Realm Command queue, SSec must be set to 0, otherwise CERROR\_ILL is raised. See 10.7 Support for Realm state .
- Virtual address fields are Address[63:12], with [11:0] taken as zero.
- Physical, or IPA address fields are Address[55:12], or [55:2] for the case of MSIAddr, with other bits taken as zero.
- -Bits[55:52] of these fields are RES0 in SMMUv3.1 to SMMUv3.3.
- -Bits[55:48] of these fields are RES0 in SMMUv3.0.

## 4.1.7 Out-of-range parameters

Providing an out-of-range parameter to a command has one of the following CONSTRAINED UNPREDICTABLE behaviors:

- The command has no effect
- The command has an effect, taking an UNPREDICTABLE value for the parameter that is out-of-range.
- -Note: For example, an implementation might truncate an out-of-range StreamID parameter to another in-range StreamID which might then be affected by the command.

See section 3.16.1.2 Command Queue . Some implementations might not provide the ability to express out-of-range values in certain fields.

A StreamID parameter for a command on the Non-secure Command queue is out of range if the value exceeds the implemented Non-secure StreamID size, as reported by SMMU\_IDR1.SIDSIZE. For a command on the Secure Command queue, a Non-secure StreamID is out of range if the value exceeds the Non-secure SMMU\_IDR1.SIDSIZE and a Secure StreamID is out of range if the value exceeds the Secure SMMU\_S\_IDR1.S\_SIDSIZE.

In an SMMU with RME DA, the size of a StreamID parameter for Realm state is the same as for the Non-secure state. This means that when submitting a command to the Realm command queue, the StreamID parameter is out of range if the value exceeds SMMU\_IDR1.SIDSIZE.

A SubstreamID parameter is out of range if the value exceeds the implemented SubstreamID size, as reported by SMMU\_IDR1.SSIDSIZE.

Address parameter ranges are described for each command type that takes an address parameter.

The allowed range of ASID and VMID parameters is covered in section 4.4 TLB invalidation .