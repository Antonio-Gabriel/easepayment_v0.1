from dataclasses import dataclass


@dataclass
class IGuardResult:
    succeeded: bool
    message: str


class Guard:
    @staticmethod
    def against_null_or_empty(argument: any, argumentName: str) -> IGuardResult:
        """Verify null or empty data"""
        if argument == None and not argumentName:
            return IGuardResult(
                succeeded=False, message="{argumentName} is null or undefined"
            )
