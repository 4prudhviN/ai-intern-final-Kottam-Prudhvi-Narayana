"""
Multi-Agent Research Pipeline - Groq Optimized
"""

from services.groq_service import generate_research

MODE_INSTRUCTIONS = {
    "Business Analysis": "Focus on market trends, competitive landscape, and business strategy.",
    "Technical Deep Dive": "Focus on technical architecture, engineering challenges, and implementation details.",
    "Startup Research": "Focus on startup opportunities, disruption potential, and venture scalability.",
    "Investor Report": "Focus on ROI, growth projections, market risks, and valuation drivers.",
    "Academic Research": "Focus on analytical rigor, historical context, and theoretical frameworks."
}

class ResearchAgent:
    def run(self, topic, mode, depth):
        mode_hint = MODE_INSTRUCTIONS.get(mode, "")
        prompt = f"""
        Conduct deep, factual research on:
        Topic: {topic}
        
        Research Mode: {mode}
        Target Depth: {depth}/10
        Instructions: {mode_hint}

        Provide a comprehensive breakdown using your internal knowledge base. Ensure technical accuracy and high information density.
        """
        return generate_research(prompt)


class TrendAnalysisAgent:
    def run(self, topic, research, mode):
        prompt = f"""
        Analyze future trends and market direction for: {topic}
        
        Research Mode: {mode}
        Research Findings: {research}

        Identify emerging patterns and potential disruptions relevant to this specific mode.
        """
        return generate_research(prompt)


class ExecutiveSummaryAgent:
    def run(self, topic, research, trends, mode):
        prompt = f"""
        Create a high-level executive summary for: {topic}
        
        Context: {mode} context
        Research Data: {research}
        Trend Data: {trends}

        Synthesize the most critical takeaways for a decision-maker.
        """
        return generate_research(prompt)
