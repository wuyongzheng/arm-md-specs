## G1.4 Execution state

The Execution states are:

AArch64

The 64-bit Execution state.

AArch32

The 32-bit Execution state.

Execution state gives more information about them.

Exception levels use Execution states. For example, EL0, EL1 and EL2 might all be using AArch32, under EL3 using AArch64.

This means that:

- Different software layers, such as an application, an operating system kernel, and a hypervisor, executing at different Exception levels, can execute in different Execution states.
- The PE can change Execution states only either:
- -At reset.
- -On a change of Exception level.

Note

- Typical Exception level usage model shows which Exception levels different software layers might typically use.
- Effect of not implementing an Exception level gives information on supported configurations of Exception levels and Execution states.

The interaction between the AArch64 and AArch32 Execution states is called interprocessing . Interprocessing describes this.

## G1.4.1 About the AArch32 PE modes

AArch32 state provides a set of PE modes that support normal software execution and handle exceptions. The current mode determines the set of registers that are available, as described in AArch32 general-purpose registers, the PC, and the Special-purpose registers.

The AArch32 modes are:

- Monitor mode. This mode always executes at Secure EL3.
- Hyp mode. This mode always executes at Non-secure EL2.
- System, Supervisor, Abort, Undefined, IRQ, and FIQ modes. The Exception level these modes execute at depends on the Security state, as described in Security state.
- User mode. This mode always executes at EL0.

Note

AArch64 state does not support modes. Modes are a concept that is specific to AArch32 state. Modes that execute at a particular Exception level are only implemented if that Exception level supports using AArch32 state.

For more information on modes, see AArch32 state PE modes.

The mode in use immediately before an exception is taken is described as the mode the exception is taken from . The mode that is used on taking the exception is described as the mode the exception is taken to .

All of the following define the mode that an exception is taken to:

- The type of exception.
- The mode the exception is taken from.
- Configuration settings defined at EL2 and EL3.

Monitor mode and Hyp mode can create system traps that cause exceptions to EL3 or EL2 respectively. There is an architected hierarchy where EL2 and EL3 configuration settings affect a common condition, for example interrupt routing. When no traps are enabled for a particular condition, the AArch32 mode an exception is taken to is called the default mode for that exception.

In AArch32 state, a number of different modes can exist at the same Exception level. All modes at a particular Exception level have the same execution privilege , meaning they have the same access rights for accesses to memory and to System registers. However, the mapping of PE modes to Exception levels depends on the Security state, as described in Security state. Security state, Exception levels, and AArch32 execution privilege gives more information about the PE modes, their associated execution privilege, and how this maps onto the Exception levels.