#!/usr/bin/env python3
"""Code audit script for syntax and standards compliance."""

import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Tuple


class CodeAuditor:
    """Code auditor for checking syntax and standards compliance."""
    
    def __init__(self, project_root: Path) -> None:
        """Initialize the code auditor.
        
        Args:
            project_root: Path to the project root directory
        """
        self.project_root = project_root
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.passed_checks: List[str] = []
        
    def run_command(self, command: List[str]) -> Tuple[int, str, str]:
        """Run a command and return the result.
        
        Args:
            command: Command to run as list of strings
            
        Returns:
            Tuple of (return_code, stdout, stderr)
        """
        try:
            result = subprocess.run(
                command,
                cwd=self.project_root,
                capture_output=True,
                text=True,
                check=False,
            )
            return result.returncode, result.stdout, result.stderr
        except FileNotFoundError:
            return 1, "", f"Command not found: {command[0]}"
            
    def check_black_formatting(self) -> bool:
        """Check code formatting with black.
        
        Returns:
            True if formatting is correct, False otherwise
        """
        print("🔍 Checking code formatting with black...")
        returncode, stdout, stderr = self.run_command([
            "black", "--check", "--diff", "benchmark", "tests"
        ])
        
        if returncode == 0:
            self.passed_checks.append("✅ Black formatting: PASSED")
            return True
        else:
            self.errors.append("❌ Black formatting: FAILED")
            if stdout:
                self.errors.append(f"Black output:\n{stdout}")
            return False
            
    def check_isort_imports(self) -> bool:
        """Check import sorting with isort.
        
        Returns:
            True if imports are sorted correctly, False otherwise
        """
        print("🔍 Checking import sorting with isort...")
        returncode, stdout, stderr = self.run_command([
            "isort", "--check-only", "--diff", "benchmark", "tests"
        ])
        
        if returncode == 0:
            self.passed_checks.append("✅ Import sorting: PASSED")
            return True
        else:
            self.errors.append("❌ Import sorting: FAILED")
            if stdout:
                self.errors.append(f"Isort output:\n{stdout}")
            return False
            
    def check_flake8_linting(self) -> bool:
        """Check code quality with flake8.
        
        Returns:
            True if linting passes, False otherwise
        """
        print("🔍 Checking code quality with flake8...")
        returncode, stdout, stderr = self.run_command([
            "flake8", "benchmark", "tests"
        ])
        
        if returncode == 0:
            self.passed_checks.append("✅ Flake8 linting: PASSED")
            return True
        else:
            self.errors.append("❌ Flake8 linting: FAILED")
            if stdout:
                self.errors.append(f"Flake8 output:\n{stdout}")
            return False
            
    def check_mypy_types(self) -> bool:
        """Check type annotations with mypy.
        
        Returns:
            True if type checking passes, False otherwise
        """
        print("🔍 Checking type annotations with mypy...")
        returncode, stdout, stderr = self.run_command([
            "mypy", "benchmark"
        ])
        
        if returncode == 0:
            self.passed_checks.append("✅ Type checking: PASSED")
            return True
        else:
            # Mypy warnings are not critical, so we classify them as warnings
            if "error:" in stdout.lower():
                self.errors.append("❌ Type checking: FAILED")
                if stdout:
                    self.errors.append(f"Mypy output:\n{stdout}")
                return False
            else:
                self.warnings.append("⚠️  Type checking: WARNINGS")
                if stdout:
                    self.warnings.append(f"Mypy output:\n{stdout}")
                return True
                
    def check_tests(self) -> bool:
        """Run tests to ensure code correctness.
        
        Returns:
            True if tests pass, False otherwise
        """
        print("🔍 Running tests...")
        returncode, stdout, stderr = self.run_command([
            "pytest", "tests/", "-v", "--tb=short"
        ])
        
        if returncode == 0:
            self.passed_checks.append("✅ Tests: PASSED")
            return True
        else:
            self.errors.append("❌ Tests: FAILED")
            if stdout:
                self.errors.append(f"Test output:\n{stdout}")
            return False
            
    def check_project_structure(self) -> bool:
        """Check project structure for best practices.
        
        Returns:
            True if structure is correct, False otherwise
        """
        print("🔍 Checking project structure...")
        
        required_files = [
            "pyproject.toml",
            "README.md",
            ".gitignore",
            "benchmark/__init__.py",
            "tests/__init__.py",
        ]
        
        missing_files = []
        for file_path in required_files:
            if not (self.project_root / file_path).exists():
                missing_files.append(file_path)
                
        if missing_files:
            self.errors.append(f"❌ Project structure: Missing files: {missing_files}")
            return False
        else:
            self.passed_checks.append("✅ Project structure: PASSED")
            return True
            
    def run_audit(self) -> bool:
        """Run the complete code audit.
        
        Returns:
            True if all checks pass, False otherwise
        """
        print("🚀 Starting code audit for syntax and standards compliance...")
        print("=" * 60)
        
        checks = [
            ("Project Structure", self.check_project_structure),
            ("Code Formatting", self.check_black_formatting),
            ("Import Sorting", self.check_isort_imports),
            ("Code Quality", self.check_flake8_linting),
            ("Type Checking", self.check_mypy_types),
            ("Tests", self.check_tests),
        ]
        
        all_passed = True
        for check_name, check_func in checks:
            try:
                if not check_func():
                    all_passed = False
            except Exception as e:
                self.errors.append(f"❌ {check_name}: ERROR - {e}")
                all_passed = False
                
        self.print_report()
        return all_passed
        
    def print_report(self) -> None:
        """Print the audit report."""
        print("\n" + "=" * 60)
        print("📊 CODE AUDIT REPORT")
        print("=" * 60)
        
        if self.passed_checks:
            print("\n✅ PASSED CHECKS:")
            for check in self.passed_checks:
                print(f"  {check}")
                
        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  {warning}")
                
        if self.errors:
            print("\n❌ FAILED CHECKS:")
            for error in self.errors:
                print(f"  {error}")
                
        print(f"\n📈 SUMMARY:")
        print(f"  Passed: {len(self.passed_checks)}")
        print(f"  Warnings: {len(self.warnings)}")
        print(f"  Errors: {len(self.errors)}")
        
        if not self.errors:
            print("\n🎉 All critical checks passed! Code meets syntax and standards requirements.")
        else:
            print("\n🔧 Please fix the errors above to meet coding standards.")


def main() -> None:
    """Main entry point for the code audit script."""
    project_root = Path(__file__).parent.parent
    auditor = CodeAuditor(project_root)
    
    success = auditor.run_audit()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()