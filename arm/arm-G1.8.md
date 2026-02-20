## G1.8 Virtualization

## G1.8.1 The effect of implementing EL2 on the Exception model

The support for virtualization described in this section applies only to an implementation that includes EL2. A PE is in Hyp mode when it is executing at EL2 in the AArch32 state. An exception return from Hyp mode to software running at EL1 or EL0 is performed using the ERET instruction.

EL2 provides a set of features that support virtualizing the Non-secure state of an A-profile implementation. The basic model of a virtualized system involves:

- Ahypervisor, running in EL2, that is responsible for switching between virtual machines . Avirtual machine is comprised of Non-secure EL1 and Non-secure EL0.

- Anumber of Guest operating systems, that each run in Non-secure EL1, on a virtual machine.

- For each Guest operating system, applications, that usually run in Non-secure EL0, on a virtual machine.

Note

In some systems, a Guest OS is unaware that it is running on a virtual machine, and is unaware of any other Guest OS. In other systems, a hypervisor makes the Guest OS aware of these facts. The architecture supports both of these models.

The hypervisor assigns a VMID to each virtual machine.

In AArch32 state, EL2 is implemented only in Non-secure state, to support Guest OS management. EL2 provides controls to:

- Provide virtual values for the contents of a small number of identification registers. A read of one of these registers by a Guest OS or the applications for a Guest OS returns the virtual value.

- Trap various operations, including memory management operations and accesses to many other registers. A trapped operation generates an exception that is taken to EL2.

- Route interrupts to the appropriate one of:

- The current Guest OS.

- AGuest OS that is not currently running.

- The hypervisor.

In Non-secure state:

- The implementation provides an independent translation regime for memory accesses from EL2.

- For the PL1&amp;0 translation regime, address translation occurs in two stages:

- Stage 1 maps the virtual address (VA) to an intermediate physical address (IPA). This is managed at EL1, usually by a Guest OS. The Guest OS believes that the IPA is the physical address (PA).

- Stage 2 maps the IPA to the PA. This is managed at EL2. The Guest OS might be unaware of this stage.

For more information on the translation regimes, see The AArch32 Virtual Memory System Architecture.

An implementation that includes EL2 implements the following exceptions:

- Hypervisor Call (HVC) exception.

- Traps to EL2. EL2 configurable controls, describes these.

- All of the virtual interrupts:

- Virtual SError.

- Virtual IRQ.

- Virtual FIQ.

HVCexceptions are always taken to EL2. All virtual interrupts are always taken to EL1, and can only be taken from Non-secure EL1 or EL0.

Each of the virtual interrupts can be independently enabled using controls at EL2.

Each of the virtual interrupts has a corresponding physical interrupt. See Virtual interrupts.

When a virtual interrupt is enabled, its corresponding physical exception is taken to EL2, unless EL3 has configured that physical exception to be taken to EL3. For more information, see Asynchronous exception behavior for exceptions taken from AArch32 state.

An implementation that includes EL2 also:

- Provides controls that can be used to route some synchronous exceptions, taken from Non-secure state, to EL2. For more information, see:
- -Routing exceptions from Non-secure EL0 to EL2.
- -Routing debug exceptions to EL2 using AArch32.
- -Routing of aborts taken to AArch32 state.
- Provides mechanisms to trap PE operations to EL2. See EL2 configurable controls. When an operation is trapped to EL2, the hypervisor typically either:
- -Emulates the required operation. The application running in the Guest OS is unaware of the trap.
- -Returns an error to the Guest OS.

## G1.8.1.1 Virtual interrupts

The virtual interrupts have names that correspond to the physical interrupts, as shown in Table G1-4.

## Table G1-4 The virtual interrupts

| Physical interrupt   | Corresponding virtual interrupt   |
|----------------------|-----------------------------------|
| External SError      | Virtual SError                    |
| IRQ                  | Virtual IRQ                       |
| FIQ                  | Virtual FIQ                       |

Software executing at EL2 can use virtual interrupts to signal physical interrupts to Non-secure EL1 and Non-secure EL0. Example G1-1 shows a usage model for virtual interrupts.

## Example G1-1 Virtual interrupt usage model

Ausage model is as follows:

1. Software executing at EL2 routes a physical interrupt to EL2.
2. When a physical interrupt of that type occurs, the exception handler executing in EL2 determines whether the interrupt can be handled in EL2 or requires routing to a Guest OS in EL1. If the interrupt requires routing to a Guest OS:
- If the Guest OS is currently running, the hypervisor uses the appropriate virtual interrupt type to signal the physical interrupt to the Guest OS.
- If the Guest OS is not currently running, the physical interrupt is marked as pending for the guest OS. When the hypervisor next switches to the virtual machine that is running that Guest OS, the hypervisor uses the appropriate virtual interrupt type to signal the physical interrupt to the Guest OS.

Non-secure EL1 and Non-secure EL0 modes cannot distinguish a virtual interrupt from the corresponding physical interrupt.

For more information, see Virtual exceptions when an implementation includes EL2.