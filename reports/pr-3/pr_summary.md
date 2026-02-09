## 🛡️ PullGuard Security Review

**Status:** ❌ FAILED

### 📊 Analysis Results

**AST Policy Violations:** 13 _(all posted, no limit)_
- 🔴 Critical: 8
- 🟠 High: 5
- 🟡 Medium: 0
- 🔵 Low: 0

**🤖 AI-Powered Code Fixes:** 13 _(max: 30)_
- Semantic error detection
- Security vulnerability fixes
- Replaceable code suggestions

### 🔍 Top Critical Issues

1. 🔴 **Dangerous use of 'eval()' detected. This can execute arbitrary code.**
   - File: `api.py:50`
   - Rule: `PY-AST-001`

2. 🔴 **Hardcoded API key detected. Use environment variables or secrets management.**
   - File: `api.py:12`
   - Rule: `PY-SECRET-001`

3. 🔴 **Command injection via os.system() with f-string. Use parameterized commands or shell=False.**
   - File: `api.py:19`
   - Rule: `PY-CMD-001`

4. 🔴 **Command injection via subprocess with shell=True. Use parameterized commands or shell=False.**
   - File: `api.py:22`
   - Rule: `PY-CMD-001`

5. 🔴 **Hardcoded password detected. Use environment variables or secrets management.**
   - File: `database.py:9`
   - Rule: `PY-SECRET-001`

---
_💡 Click on AI suggestions in inline comments to apply fixes directly_

*Powered by [PullGuard](https://github.com/sristikulkarni-gif/PullGuardProject) - Azure AI Security Analysis*
