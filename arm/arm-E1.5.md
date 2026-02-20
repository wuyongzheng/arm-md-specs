## E1.5 Exceptions

The Arm architecture uses the following terms to describe various types of exceptional condition:

## Exceptions

In the Arm architecture, an exception causes entry to EL1, EL2, or EL3. If the Exception level that is entered is using AArch32, it also causes entry to the PE mode in which the exception must be taken. A software handler for the exception is then executed.

Note

The term floating-point exception does not use this meaning of exception . This term is described later in this list.

## Exceptions include:

- Reset.
- Interrupts.
- Memory system aborts.
- Undefined instructions.
- Supervisor calls (SVCs), Secure Monitor calls (SMCs), and Hypervisor calls (HVCs).
- Debug exceptions.

Most details of exception handling are not visible to application level software, and are described in Handling exceptions that are taken to an Exception level using AArch32. In an implementation that includes all the Exception levels, aspects that are visible to application level software are:

- The SVC instruction causes a Supervisor Call exception. This provides a mechanism for unprivileged software to make a call to the operating system, or other system component that is accessible only at EL1.
- The SMC instruction causes a Secure Monitor Call exception, but only if software execution is at EL1 or higher. Unprivileged software can only cause a Secure Monitor Call exception by methods defined by the operating system, or by another component of the software system that executes at EL1 or higher.
- The HVC instruction causes a Hypervisor Call exception, but only if software execution is at EL1 or higher. Unprivileged software can only cause a Hypervisor Call exception by methods defined by the hypervisor, or by another component of the software system that executes at EL1 or higher.
- The BKPT instruction causes a Breakpoint Instruction exception, which is taken as a Prefetch Abort exception. This provides a mechanism for a debugger to insert breakpoints into unprivileged software, or for unprivileged software to make a call into a debugger that is accessible at EL1.
- The WFI (Wait for Interrupt) instruction provides a hint that nothing needs to be done until an interrupt or another WFI wakeup event occurs, see Wait For Interrupt. This means the hardware might enter a low-power state until the wakeup event occurs.
- The WFE (Wait for Event) instruction provides a hint that nothing needs to be done until either an SEV instruction generates an event, or another WFE wakeup event occurs, see Wait For Event and Send Event. This means the hardware might enter a low-power state until the wakeup event occurs.

## Floating-point exceptions

These relate to exceptional conditions encountered during floating-point arithmetic, such as Divide by Zero or Overflow. For more information, see:

- Floating-point exceptions and exception traps.
- The FPEXC and FPSCR register descriptions.
- ANSI/IEEE Std. 754, IEEE Standard for Binary Floating-Point Arithmetic .

## Chapter E2 The AArch32 Application Level Memory Model

This chapter gives an application level description of the memory model for software executing in AArch32 state. This means it describes the memory model for execution in EL0 when EL0 is using AArch32 in the following sections:

- About the Arm memory model.
- Atomicity in the Arm architecture.
- Definition of the memory model.
- Ordering of translation table walks.
- Caches and memory hierarchy.
- Alignment support.
- Endian support.
- Memory types and attributes.
- Mismatched memory attributes.
- Synchronization and semaphores

Note

In this chapter, System register names usually link to the description of the register in AArch32 System Register Descriptions, for example SCTLR.