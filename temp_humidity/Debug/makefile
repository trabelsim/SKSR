################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include Drivers/STM32L4xx_HAL_Driver/Src/subdir.mk
-include Core/Startup/subdir.mk
-include Core/Src/subdir.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 
EXECUTABLES += \
temp_humidity.elf \

SIZE_OUTPUT += \
default.size.stdout \

OBJDUMP_LIST += \
temp_humidity.list \

OBJCOPY_BIN += \
temp_humidity.bin \


# All Target
all: temp_humidity.elf secondary-outputs

# Tool invocations
temp_humidity.elf: $(OBJS) $(USER_OBJS) C:\Users\Maroine\ Trabelsi\Desktop\Sterowniki\temp_humidity\STM32L476RGTX_FLASH.ld
	arm-none-eabi-gcc -o "temp_humidity.elf" @"objects.list" $(USER_OBJS) $(LIBS) -mcpu=cortex-m4 -T"C:\Users\Maroine Trabelsi\Desktop\Sterowniki\temp_humidity\STM32L476RGTX_FLASH.ld" --specs=nosys.specs -Wl,-Map="temp_humidity.map" -Wl,--gc-sections -static -u _printf_float --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -u _printf_float -u _scanf_float -Wl,--start-group -lc -lm -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

default.size.stdout: $(EXECUTABLES)
	arm-none-eabi-size  $(EXECUTABLES)
	@echo 'Finished building: $@'
	@echo ' '

temp_humidity.list: $(EXECUTABLES)
	arm-none-eabi-objdump -h -S $(EXECUTABLES) > "temp_humidity.list"
	@echo 'Finished building: $@'
	@echo ' '

temp_humidity.bin: $(EXECUTABLES)
	arm-none-eabi-objcopy  -O binary $(EXECUTABLES) "temp_humidity.bin"
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) *
	-@echo ' '

secondary-outputs: $(SIZE_OUTPUT) $(OBJDUMP_LIST) $(OBJCOPY_BIN)

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets
