---
name: cv-optimizer
description: |
  5-step CV/resume optimizer: expert matching → JD analysis → CV gap diagnosis (with real analytics data) → optimization strategy → full rewrite with quantified achievements → PDF + Notion output. Uses Austin Belcak's achievement quantification framework. Triggers on: "幫我改CV", "優化CV", "CV優化", "optimize CV", "tailor CV", "rewrite CV", "幫我寫CV", "改履歷", "履歷優化", "resume optimization", "apply for this job", "幫我申請呢份工", "CV針對呢個JD", "度身訂造CV", or when user provides a JD and CV together. Also triggers when user pastes a job posting and says "我想申請" or "help me apply". Requires WebSearch, Chrome browser tools, PDF skill, and optionally Notion MCP.
---

# CV Optimizer — Expert-Guided 5-Step Framework

## Overview

This skill transforms a generic CV into a highly targeted, ATS-optimized document for a specific job application. It follows a structured 5-step process with human confirmation at each stage, ensuring the applicant understands every optimization decision.

The core philosophy comes from Austin Belcak (Cultivated Culture): every bullet point must answer "So what? Prove it." with quantified results.

## Prerequisites

Before starting, gather these inputs from the user:

- **Job Description (JD)** — the full text of the target position
- **Current CV** — uploaded as PDF or pasted text
- **Target company name** (if available)
- **Target region** (for cultural formatting norms)
- **Any supplementary materials** — screenshots of tools, analytics dashboards, portfolio links

If the user has a YouTube channel or other measurable online presence relevant to the role, offer to pull real analytics data via browser tools (YouTube Studio, Instagram Insights, etc.) to strengthen the CV with verified metrics.

## The 5-Step Process

Each step must be completed and confirmed by the user before proceeding to the next. If the user requests changes at any step, revise that step before continuing.

---

### Step 0: Expert Matching (Pre-Step)

This step establishes the analytical lens for the entire process.

1. **Analyse the task** — identify the target role's industry, required skills, and regional job market norms
2. **Search for real CV experts** — use WebSearch to find 3 real, verifiable CV strategists with published credentials. Prioritise experts whose methodology matches the role type (e.g., data-driven roles → quantification-focused experts, creative roles → portfolio/storytelling experts)
3. **Present candidates** — show the user a recommended expert plus 2 alternatives, each with: real name, institution, credentials, methodology style, and why they fit this application
4. **Adopt the expert's framework** — once the user confirms, establish that expert's analytical perspective for all subsequent steps

Default recommendation: **Austin Belcak** (Cultivated Culture) for data/analytics/tech roles, due to his achievement quantification methodology and analysis of 125,000+ resumes.

---

### Step 1: Deep JD Analysis

Analyse the job description through the chosen expert's lens:

**1.1 Requirements Extraction**
- Must-Have skills (5-8 items with importance ratings)
- Nice-to-Have skills (3-5 items)
- Hidden requirements (read between the lines — culture signals, implicit priorities, role positioning)

**1.2 ATS Keyword Identification**
- High-frequency functional keywords
- Industry tools and platform names
- Soft skill keywords

**1.3 Company Culture Signals**
- Infer the ideal candidate profile from JD language and tone
- Identify whether the role is execution-focused, strategy-focused, or hybrid
- Note any contradictions in the JD (common in outsourced/agency postings)

**Output format:** Present as a structured table with "Must-Have vs Nice-to-Have vs Hidden Requirements" plus an ATS keyword checklist.

Pause and wait for user confirmation: "✋ 步驟 1 完成。請確認分析是否準確，輸入「繼續」進入步驟 2。"

---

### Step 2: Deep CV Analysis

Review the current CV as if you were the hiring manager screening 200 applications:

**2.1 Strengths**
- Which experiences and achievements are most competitive?
- Which quantified results would most impress a recruiter?

**2.2 Gaps and Weaknesses**
- Missing JD keywords
- Vague descriptions lacking quantification
- Format/length issues for the target market
- Misaligned positioning (e.g., CV title doesn't match the target role)

**2.3 Data Collection (if applicable)**
- If the user has a YouTube channel, website, or other measurable platform relevant to the role, ask permission to access their analytics dashboard via browser tools
- Pull real metrics: subscribers, views, CTR, retention, engagement rates, growth percentages
- These verified numbers become powerful ammunition for the optimised CV

**2.4 Fit Score**
- Overall match: X/10
- Dimension scores: Skill Match / Experience Relevance / Keyword Coverage / Expression Quality

**Output format:** Three-column checklist (✅ Strengths | ⚠️ Needs Work | ❌ Missing) plus fit score table.

Pause and wait for user confirmation.

---

### Step 3: Optimization Strategy

Synthesise Step 1 (JD) + Step 2 (CV) + any collected analytics data into a targeted action plan:

**3.1 Priority Ranking**
- High priority (determines whether CV passes initial screening)
- Medium priority (affects interview invitation rate)
- Low priority (nice-to-have polish)

**3.2 Achievement Reframing Plan**
Using the CAR method (Context → Action → Result + Data):
- Identify which experiences need rewriting
- Specify what quantified data to add
- Show before/after direction for key bullet points

**3.3 ATS Keyword Integration Plan**
- Map each JD keyword to a specific CV section for natural placement
- Ensure no keyword stuffing — every keyword must appear in a meaningful context

**3.4 Structural Recommendations**
- Recommended CV structure and section order
- Sections to add, remove, or reorganise
- Target page count (1 or 2 pages based on experience level and market norms)

Pause and wait for user confirmation.

---

### Step 4: Write the Optimised CV

Following the confirmed strategy, write the complete CV in Markdown:

**Structure (adapt to target market):**
1. Header — Name, target role title, contact details, portfolio links
2. Professional Summary — 3-4 lines with core value proposition, years of experience, and key metrics
3. Core Competencies — Keyword-dense skills grid, ATS-optimised
4. Professional Experience — CAR-method bullet points, every achievement quantified
5. Certifications — Select only the most relevant (3-5 max)
6. Education
7. Languages (if relevant)

**Writing Rules:**
- All content must come from the applicant's real experience — never fabricate
- Every achievement bullet must contain: specific action verb + quantified result
- Naturally embed all ATS keywords identified in Step 1
- Match the language and cultural conventions of the target job market
- Remove: salary expectations, irrelevant 90-day plans for other companies, residency status (unless specifically requested by JD)

Present the full CV text for user review. Pause and wait for confirmation.

---

### Step 5: Generate Deliverables

**5.1 PDF Generation**
- Use reportlab to create a professional, ATS-readable PDF
- A4 size, clean fonts (Helvetica), teal accent colour scheme
- File naming: `[Name]_CV_[Target_Role]_[Date].pdf`
- Save to workspace folder

**5.2 Notion Save (if Notion MCP available)**
- Create the CV as a Notion page
- Organise under 📁 文件 / 💼 LinkedIn 求職 folder (create if needed)

**5.3 Completion Package**
Present to the user:
- PDF download link
- Notion page link (if applicable)
- Submission checklist (CV ✅, Cover Letter status, Portfolio link check)
- 3 interview preparation tips specific to this role

---

## Key Principles

**Data over claims.** Always prefer verified metrics from real dashboards over self-reported estimates. If the user has YouTube Studio, Google Analytics, or any other analytics platform accessible via browser, pull the real numbers.

**Positioning over polishing.** The biggest impact comes from repositioning the CV's narrative to match what the JD is actually asking for, not from wordsmithing individual sentences.

**The "So what?" test.** Every bullet point must survive the question: "So what? Why should the hiring manager care?" If it can't, it needs a quantified result or should be removed.

**Respect the user's truth.** Never add experiences, skills, or achievements the user hasn't mentioned. Ask for clarification rather than assume.

## Example Trigger Scenarios

- User pastes a LinkedIn job posting and says "幫我改CV申請呢份工"
- User uploads their CV and a JD and says "optimize this for me"
- User says "我想申請 YouTube Channel Manager 呢個位，幫我tailor CV"
- User provides screenshots of their analytics tools alongside their CV

---

## 多智能體事實紀律模式（v2.0 新增 — 必讀）

**任何涉及公司審視、行業分析、unit economics 推導、或用戶講「唔好吹水／要市場數據」嘅步驟，必須先 Read `knowledge/fact-discipline.md` 並照行。**

核心規則摘要（詳見 knowledge 檔）：

1. **總指揮 + 4 現實真人 subagent 並行**（Agent tool，general-purpose）：① Unit Economics（McCarthy/Fader CBCV）② 行業營運模式（該行業最有公開披露嘅營運者，如 Trupanion）③ 薪酬+市場數據核實（Michael Page / Morgan McKinley / 政府統計 > aggregator）④ 策略合成（Alison Green 視角）
2. **每個數字要 URL，搵唔到標 UNVERIFIED**，唔准填數
3. **證據四級分級**：【公開】【基準】【推導】【評分】—— 推導模型「做問題，唔做答案」
4. **Locked lessons**：分母口徑先於計算；幾何壽命模型要對 cohort 披露；市場規模用龍頭收入 sanity check；重建必出 v1→v2 更正表

呢個模式係 2026-07-31 Codex 獨立審視捉到多處推導錯誤後 lock 入嚟嘅 —— 同一個錯誤唔教第二次。
