from flask import Flask, request, render_template, session, redirect, url_for
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

def get_gemini_review(code, api_key):
    """
    Sends code to the Gemini API for review.
    """
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro-latest')
        
        prompt = f"""
        Please act as an expert code reviewer. Review the following code and provide feedback on these criteria in the exact markdown format provided below. Fill in all sections thoroughly. Use 'language' as a placeholder for the programming language of the code being reviewed in code blocks.

        Here is the code:
        ---
        {code}
        ---

        # 🔍 DeepCode Review Report

        ---

        ## 📊 Code Quality Score

        **Overall Rating: [X/10]** ⭐⭐⭐⭐⭐⭐⭐☆☆☆

        ```
        ██████████░░░░░░░░░░ 70%
        ```

        | Category | Score | Status |
        |----------|-------|--------|
        | Syntax | [X/10] | 🟢 Good / 🟡 Fair / 🔴 Poor |
        | Performance | [X/10] | 🟢 Good / 🟡 Fair / 🔴 Poor |
        | Best Practices | [X/10] | 🟢 Good / 🟡 Fair / 🔴 Poor |
        | Readability | [X/10] | 🟢 Good / 🟡 Fair / 🔴 Poor |
        | Security | [X/10] | 🟢 Good / 🟡 Fair / 🔴 Poor |

        **Complexity Level:** Low / Medium / High
        **Estimated Fix Time:** [X] minutes

        ---

        ## 🎯 Executive Summary

        [Brief 2-3 sentence overview of the code quality and main findings]

        ---

        ## ❌ Critical Issues (Must Fix)

        ### Issue #1: [Issue Title]
        **Severity:** 🔴 Critical / 🟡 Medium / 🟢 Low
        **Line(s):** [Line numbers: e.g., 5, 10-12]
        **Impact:** [What problem this causes]

        **Current Code:**
        ```language
        [problematic code snippet]
        ```

        **Problem:**
        - [Explanation point 1]
        - [Explanation point 2]

        **Solution:**
        ```language
        [corrected code snippet]
        ```

        **Why This Fix Works:**
        [Brief explanation of the solution]

        ---

        ### Issue #2: [Issue Title]
        [Repeat structure above for each critical issue]

        ---

        ## ⚠️ Warnings (Should Fix)

        ### Warning #1: [Warning Title]
        **Severity:** 🟡 Medium
        **Line(s):** [Line numbers: e.g., 15]

        **What to improve:**
        - [Point 1]
        - [Point 2]

        **Suggested Fix:**
        ```language
        [improved code]
        ```

        ---

        ## ⚡ Performance Suggestions

        ### Optimization #1: [Title]
        **Current Approach:** [Description]
        **Issue:** [Performance bottleneck]
        **Better Approach:** [Optimized solution]

        **Before:**
        ```language
        [slower code]
        ```

        **After:**
        ```language
        [optimized code]
        ```

        **Expected Improvement:** [X%] faster / [X] MB less memory

        ---

        ## ✅ What's Working Well

        - ✓ [Positive aspect 1]
        - ✓ [Positive aspect 2]
        - ✓ [Positive aspect 3]

        ---

        ## 🔐 Security Analysis

        **Security Score:** [X/10] 🔒

        | Check | Status | Notes |
        |-------|--------|-------|
        | Input Validation | ✅ Pass / ❌ Fail | [Comment] |
        | SQL Injection Risk | ✅ Pass / ❌ Fail | [Comment] |
        | XSS Protection | ✅ Pass / ❌ Fail | [Comment] |
        | Authentication | ✅ Pass / ❌ Fail | [Comment] |
        | Data Exposure | ✅ Pass / ❌ Fail | [Comment] |

        **Vulnerabilities Found:** [Number]

        ---

        ## 📚 Best Practices Check

        ### Naming Conventions
        - [✅/❌] Variables use descriptive names
        - [✅/❌] Functions follow naming standards
        - [✅/❌] Classes use proper casing

        ### Code Structure
        - [✅/❌] Proper indentation
        - [✅/❌] Logical organization
        - [✅/❌] Single Responsibility Principle

        ### Documentation
        - [✅/❌] Comments explain complex logic
        - [✅/❌] Functions have descriptions
        - [✅/❌] README or documentation exists

        ---

        ## 🎨 Code Style & Readability

        **Readability Score:** [X/10] 📖

        **Strengths:**
        - [Strength 1]
        - [Strength 2]

        **Areas for Improvement:**
        - [Improvement 1]
        - [Improvement 2]

        ---

        ## 💡 Refactoring Suggestions

        ### Suggestion #1: [Title]
        **Current Complexity:** High / Medium / Low
        **Proposed Refactor:**

        ```language
        // Current approach
        [current code]

        // Refactored approach
        [improved code]
        ```

        **Benefits:**
        - [Benefit 1]
        - [Benefit 2]

        ---

        ## 🧪 Testing Recommendations

        - [ ] Add unit tests for [function/module]
        - [ ] Test edge cases: [specific cases]
        - [ ] Add error handling tests
        - [ ] Consider integration tests for [feature]

        ---

        ## 📦 Dependencies & Compatibility

        **Language Version:** [Version]
        **Dependencies Found:** [Number]

        | Dependency | Version | Status | Notes |
        |------------|---------|--------|-------|
        | [Package] | [X.X.X] | ✅ Updated / ⚠️ Outdated | [Comment] |

        ---

        ## 🚀 Quick Wins (Easy Fixes)

        1. **[Fix 1]** - Estimated time: [X] min
           ```language
           [code example]
           ```

        2. **[Fix 2]** - Estimated time: [X] min
           ```language
           [code example]
           ```

        3. **[Fix 3]** - Estimated time: [X] min
           ```language
           [code example]
           ```

        ---

        ## 📈 Before & After Comparison

        ### Original Code Quality: [X/10]
        ### After Applying Fixes: [X/10] (Expected)

        **Improvement:** +[X] points

        ---

        ## 🎓 Learning Resources

        Based on the issues found, consider reviewing:
        - [Resource 1] - [Link or description]
        - [Resource 2] - [Link or description]
        - [Resource 3] - [Link or description]

        ---

        ## 🎯 Action Plan

        ### Priority 1 (Fix Now - Critical)
        1. [Action item 1]
        2. [Action item 2]

        ### Priority 2 (Fix Soon - Important)
        1. [Action item 1]
        2. [Action item 2]

        ### Priority 3 (Nice to Have)
        1. [Action item 1]
        2. [Action item 2]

        ---

        ## 📝 Final Notes

        [Any additional comments, recommendations, or context-specific advice]

        ---

        ## 📞 Next Steps

        1. **Review** the critical issues marked with 🔴
        2. **Apply** the suggested fixes from the "Quick Wins" section
        3. **Test** your code after making changes
        4. **Re-submit** for another review if needed

        ---

        **Review Generated:** [Date/Time]
        **Review ID:** #[XXXX]
        **Powered by:** DeepCode Reviewer AI

        ---

        💬 **Questions about this review?** Submit your code again with specific questions in comments!
        """

        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error calling Gemini API: {e}"

@app.route('/')
def index():
    theme = session.get('theme', 'dark') # Default to dark theme
    if theme == 'dark':
        return render_template('index_dark.html')
    else:
        return render_template('index_light.html')

@app.route('/toggle_theme')
def toggle_theme():
    current_theme = session.get('theme', 'dark')
    if current_theme == 'dark':
        session['theme'] = 'light'
    else:
        session['theme'] = 'dark'
    return redirect(url_for('index'))

@app.route('/review', methods=['POST'])
def review():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY environment variable not set.", 500

    code = request.form.get('code')
    if not code:
        return "Error: No code provided for review.", 400

    review_result = get_gemini_review(code, api_key)
    return review_result

if __name__ == '__main__':
    app.run(debug=True)
