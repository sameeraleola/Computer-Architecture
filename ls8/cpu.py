"""
Day 2: Add the ability to load files dynamically, get mult.ls8 running
 x Un-hardcode the machine code
 x Implement the load() function to load an .ls8 file given the filename passed in as an argument
 Implement a Multiply instruction (run mult.ls8)
"""
import sys

class CPU:
    """Main CPU class."""

    """Construct a new CPU."""
    def __init__(self):
        # RAM
        self.ram = [0] * 256
        # CPU registers
        self.reg = [0] * 8
        # Program counter
        self.pc = 0
        # Instruction register
        self.ir = 0
        # Memory address register
        # self.mar = 0
        # Memory data register
        # self.mdr = 0

        self
        self.opcodes = {
        # Check the opcode for the following information:
        # 1. Bits 6-7: Number of operands for the opcode 0, 1, or 2
        # 2. Bit 5 ALU or CPU
        # 3. Bit 4 if the operand sets the PC or jumps
        # 4. Bits 0-2 the opcode identifier
            0b10000010: self.ldi,
            0b01000111: self.prn,
            0b10100010: self.mul, # 4th bit defines set (0) for increment or jump (1)
            0b00000001: self.hlt
        }

    # def _cora(self, op):
    #     mask = op &

    ### CPU opcodes ###
    # LDI: Load immediate = Load the data in mdr into the register specified in mar
    def ldi(self, mar, mdr):
        self.reg[mar] = mdr
        self.pc += 3

    # PRN: print the value in the register specified in mar
    def prn(self, mar, mdr):
        print(self.reg[mar])
        self.pc += 2

    # MUL: Multiple in ALU
    def mul(self, mar, mdr):
        self.alu("MUL", mar, mdr)
    
    # ADD: Add in ALU
    def add(self, mar, mdr):
        self.alu("ADD", mar, mdr)

    # hlt: Exit the executing program
    def hlt(self, mar, mdr):
        exit(0)


    # Read the value stored in memory location adr
    def ram_read(self, mar):
        return self.ram[mar]

   # Write the value (mdr) the value stored in memory location adr
    def ram_write(self, mdr, mar):
        self.ram[mar] = mdr

    def pcinc(self, opcode):
        print(f'PC coming in: {self.pc}')
        print(bin(opcode))
        


    def load(self, programfile):
        """Load a program into memory."""
        address = 0

        # Open and parsee the program file
        with open(programfile) as program:
            for instruction in program:
                # print(f'instruction read = {instruction}')
                line_read = instruction.split("#")[0].strip()
                if line_read == '':
                    continue
                prog_step = int(line_read, 2)
                # print(prog_step)
                self.ram[address] = prog_step
                # print(f'ram[{address}] = {self.ram[address]}')
                address += 1


    """Run the CPU."""
    def run(self):
        while True:
            print(f'Start PC: {self.pc}')
            # Initialize the program
            self.ir = self.ram[self.pc]
            # Cache the first two values in memory
            op_a = self.ram[self.pc + 1]
            op_b = self.ram[self.pc + 2]

            # Execute the opcode in the opcode dict
            self.opcodes[self.ir](op_a, op_b)
            # set or increment PC
            # Set or PC increment
            self.pcinc(self.ir)
            print(f'PC at the bottom: {self.pc}')

    # Implement the ALU
    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")


    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    # def run(self):
    #     """Run the CPU."""
    #     pass
