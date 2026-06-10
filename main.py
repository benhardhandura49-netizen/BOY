import flet as ft


def main(page: ft.Page):
    page.title = "Engineering Portfolio - Confidence in Concepts"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # ========== PROJECT TIMELINE ==========
    # ========== PROJECT TIMELINE (UPDATED FOR FIREBASE MANAGER) ==========
    timeline_entries = [
        {"week": 1, "date": "Feb 24 - Mar 02", "contributions": "Initialized Firebase project & configured SDK data connection metrics in Flet."},
        {"week": 2, "date": "Mar 03 - Mar 09", "contributions": "Structured NoSQL Firestore collection schemas for quotation calculation models."},
        {"week": 3, "date": "Mar 10 - Mar 16", "contributions": "Programmed CRUD pipelines to capture live data arrays from engineering modules."},
        {"week": 4, "date": "Mar 17 - Mar 23", "contributions": "Deployed Firebase Authentication hooks for safe user sign-in & team workspaces."},
        {"week": 5, "date": "Mar 24 - Mar 30", "contributions": "Wrote Firestore Security Rules to protect client pricing sheets from unauthorized writes."},
        {"week": 6, "date": "Mar 31 - Apr 06", "contributions": "Optimized database query speeds via indexing and handled real-time listener streams."},
        {"week": 7, "date": "Apr 07 - Apr 13", "contributions": "Built data serialization functions to fix async race conditions in cost totals."},
        {"week": 8, "date": "Apr 14 - Apr 20", "contributions": "Finalized backend environment stress-testing, data logs, and live app staging."}
    ]

    def build_timeline():
        cards = []
        for e in timeline_entries:
            cards.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Text("📅", size=20),
                                        ft.Text(f"Week {e['week']}: {e['date']}", weight=ft.FontWeight.BOLD),
                                    ]
                                ),
                                ft.Text(e["contributions"]),
                            ],
                            spacing=10,
                        ),
                        padding=12,
                    )
                )
            )
        return ft.Column([
            ft.Text("📅 Weekly Contributions", size=24, weight=ft.FontWeight.BOLD),
            ft.Column(cards, spacing=10),
        ])

    # ========== ACTUAL MATLAB CERTIFICATES WITH CONVERTED IMAGES ==========
    matlab_courses = [
        {"name": "MATLAB Onramp", "date": "2026-04-24", "code": "MLC-ONRAMP", "progress": "100%", "img": "matlab_onramp.png"},
        {"name": "Calculations with Vectors and Matrices", "date": "2026-04-24", "code": "MLC-VECMAT", "progress": "100%", "img": "vectors_matrices.png"},
        {"name": "Make and Manipulate Matrices", "date": "2026-04-24", "code": "MLC-MATMAN", "progress": "100%", "img": "manipulate_matrices.png"},
        {"name": "Explore Data with MATLAB Plots", "date": "2026-04-28", "code": "MLC-PLOTS", "progress": "100%", "img": "matlab_plots.png"},
        {"name": "Machine Learning Onramp", "date": "2026-04-28", "code": "MLC-MLON", "progress": "100%", "img": "ml_onramp.png"},
        {"name": "MATLAB Desktop Tools and Troubleshooting Scripts", "date": "2026-04-28", "code": "MLC-DTTOOL", "progress": "100%", "img": "desktop_tools.png"},
        {"name": "Simulink Fundamentals", "date": "2026-04-28", "code": "MLC-SIMFUN", "progress": "4%", "img": "simulink_fundamentals.png"},
    ]

    def build_matlab_hub():
        grid = []
        
        # Interactive full-screen popup viewer modal window (Enlarged to 700px height for ultimate clarity)
        cert_dialog = ft.AlertDialog(
            content=ft.Image(src="", fit=ft.BoxFit.CONTAIN, height=700),
            actions=[ft.TextButton("Close", on_click=lambda e: page.pop_dialog())]
        )

        def show_certificate(e, img_src):
            cert_dialog.content.src = f"/{img_src}"
            page.show_dialog(cert_dialog)
            page.update()

        for course in matlab_courses:
            is_complete = course["progress"] == "100%"
            badge_text = "Verified (100%)" if is_complete else f"In Progress ({course['progress']})"
            badge_color = ft.Colors.GREEN_100 if is_complete else ft.Colors.ORANGE_100
            badge_text_color = ft.Colors.GREEN_700 if is_complete else ft.Colors.ORANGE_700

            grid.append(ft.Container(
                content=ft.Column([
                    # 1. ENLARGED IMAGE CONTAINER: Height boosted from 130 to 200 for maximum visibility
                    ft.Container(
                        content=ft.Image(
                            src=f"/{course['img']}",
                            fit=ft.BoxFit.CONTAIN, # Keeps the entire certificate visible without cropping it out
                            border_radius=6,
                            error_content=ft.Icon(ft.icons.Icons.BROKEN_IMAGE, size=40, color=ft.Colors.GREY_400)
                        ),
                        height=200, # Significantly taller to make text legible
                        alignment=ft.Alignment.CENTER,
                        bgcolor=ft.Colors.WHITE, # White background blends perfectly with the certificate margins
                        border_radius=6,
                    ),
                    ft.Divider(height=1, color=ft.Colors.GREY_200), # Clean separator line
                    ft.Text(
                        course["name"], 
                        size=13, 
                        weight=ft.FontWeight.BOLD, 
                        text_align=ft.TextAlign.CENTER,
                        max_lines=2,
                        overflow=ft.TextOverflow.ELLIPSIS
                    ),
                    ft.Text(f"Date: {course['date']}", size=11),
                    ft.Text(f"Code: {course['code']}", size=9, font_family="monospace"),
                    ft.Chip(
                        label=ft.Text(badge_text, size=10, color=badge_text_color, weight=ft.FontWeight.BOLD), 
                        bgcolor=badge_color
                    )
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                padding=12, 
                border=ft.Border.all(1, ft.Colors.GREY_300), 
                border_radius=10, 
                width=320, # 2. WIDER CARDS: Expanded card width from 220 to 320 to match the aspect ratio of a landscape certificate
                on_click=lambda e, img=course["img"]: show_certificate(e, img),
                ink=True 
            ))
            
        return ft.Column([
            ft.Text("📜 MathWorks Learning Center Verification", size=24, weight=ft.FontWeight.BOLD),
            # 3. RESPONSIVE GRID CONFIG: Bumped max_extent up to 340 so cards can spread out cleanly across the monitor screen
            ft.GridView(controls=grid, runs_count=3, max_extent=340, spacing=16, expand=True)
        ], scroll=ft.ScrollMode.AUTO)

    # ========== TECHNICAL BLOG ==========
    # ========== ELECTRONICS TECHNICAL BLOG ==========
    # ========== ELECTRONICS TECHNICAL BLOG ==========
    # ========== ENGINEERED TECHNICAL BLOG ==========
    def build_blog():
        # High-end typography labels for formulas
        eq1 = ft.Text("fᵣ = 1 / (2π × √(L × C))", font_family="monospace", size=15, color=ft.Colors.CYAN_400, weight=ft.FontWeight.BOLD)
        eq2 = ft.Text("Z_max = R", font_family="monospace", size=15, color=ft.Colors.AMBER_400, weight=ft.FontWeight.BOLD)

        # TECHNICAL POST 1: Parallel Resonance
        post1 = ft.Container(
            content=ft.Column([
                # Header row with structural badge icon accents
                ft.Row([
                    ft.Icon(ft.icons.Icons.BOLT, color=ft.Colors.CYAN_400, size=24),
                    ft.Text("Resonant Frequency in Parallel RLC Networks", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
                ], spacing=10),
                
                ft.Text(
                    "In an ideal AC parallel RLC circuit, resonance occurs when inductive reactance equals capacitive reactance. "
                    "At this specific point, the reactive elements cancel each other out out-of-phase.", 
                    size=14, color=ft.Colors.BLUE_GREY_700
                ),
                
                # Split-screen view layout design pattern (Text information vs Schematic Diagram)
                ft.ResponsiveRow([
                    # Left side text data block
                    ft.Column([
                        ft.Text("Mathematical Derivation Block:", size=12, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_400),
                        ft.Container(
                            content=eq1,
                            padding=12,
                            bgcolor=ft.Colors.GREY_900, # Sleek dark mode terminal terminal background
                            border_radius=6,
                            alignment=ft.Alignment.CENTER
                        ),
                        ft.Text("Where fᵣ = resonant frequency (Hz), L = inductance (H), and C = capacitance (F).", size=12, italic=True),
                    ], col={"sm": 12, "md": 6}),
                    
                    # Right side circuit image blueprint canvas container
                    ft.Column([
                        ft.Text("Network Configuration Schematic:", size=12, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_400),
                        ft.Container(
                            content=ft.Image(
                                src="/rlc_circuit.png",
                                fit=ft.BoxFit.CONTAIN,
                                error_content=ft.Icon(ft.icons.Icons.BOLT, size=40, color=ft.Colors.CYAN_200) # Fallback vector graphic
                            ),
                            height=110,
                            bgcolor=ft.Colors.WHITE,
                            border=ft.Border.all(1, ft.Colors.CYAN_100),
                            border_radius=6,
                            alignment=ft.Alignment.CENTER
                        )
                    ], col={"sm": 12, "md": 6})
                ], spacing=15),
                
                # Video Analysis Frame Window Component
                ft.Text("🎥 Media Insert: Parallel Resonance Phase Vectors", size=12, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_400),
                ft.Container(
                    content=ft.Text("Video placeholder: https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"),
                    border_radius=8,
                )
            ], spacing=12),
            padding=20,
            border=ft.Border.all(1, ft.Colors.GREY_200),
            border_radius=12,
            bgcolor=ft.Colors.WHITE,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.with_opacity(0.05, ft.Colors.BLACK))
        )

        # TECHNICAL POST 2: Impedance tracking
        post2 = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Icon(ft.icons.Icons.ANALYTICS, color=ft.Colors.AMBER_700, size=24),
                    ft.Text("Maximum Impedance and Bandwidth Tracking", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
                ], spacing=10),
                
                ft.Text(
                    "At parallel resonance, the total mathematical impedance of the network reaches its absolute peak value, "
                    "simplifying directly to purely resistive behavior as reactive admittance drops to zero.", 
                    size=14, color=ft.Colors.BLUE_GREY_700
                ),
                
                ft.Text("Purely Resistive Characteristic Node:", size=12, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_400),
                ft.Container(
                    content=eq2,
                    padding=12,
                    bgcolor=ft.Colors.GREY_900,
                    border_radius=6,
                    width=200
                ),
                
                ft.Text(
                    "By deploying sweeping frequency loops via Python arrays, we can automate tracking curves "
                    "to extract structural parameters like Quality Factor (Q) and half-power cutoff points dynamically.",
                    size=14, color=ft.Colors.BLUE_GREY_700
                ),
                
                ft.Text("📹 Simulation Tutorial: Plotting Impedance Sweeps", size=12, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_400),
                ft.Container(
                    content=ft.Text("Video placeholder: https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WhatCar.mp4"),
                    border_radius=8,
                )
            ], spacing=12),
            padding=20,
            border=ft.Border.all(1, ft.Colors.GREY_200),
            border_radius=12,
            bgcolor=ft.Colors.WHITE,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.with_opacity(0.05, ft.Colors.BLACK))
        )

        return ft.Column([
            ft.Text("✍️ Technical Blog: Confidence in Concepts", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_900),
            ft.Text("Academic portfolio notes applying core circuit calculations to Python automated programming configurations.", size=14, color=ft.Colors.BLUE_GREY_500),
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
            post1, 
            ft.Divider(height=15, color=ft.Colors.TRANSPARENT),
            post2
        ], scroll=ft.ScrollMode.AUTO)

    # ========== GITHUB EVIDENCE ==========
    commits = [
        {"hash": "a1b2c3d", "date": "2026-02-28", "msg": "feat: mining cost calculator"},
        {"hash": "e4f5g6h", "date": "2026-03-05", "msg": "fix: civil load simulation overflow"},
        {"hash": "i7j8k9l", "date": "2026-03-12", "msg": "docs: MATLAB cert verification"},
        {"hash": "m0n1o2p", "date": "2026-03-18", "msg": "test: metallurgical yield function"},
    ]
    prs = [
        {"id": 24, "title": "Material cost estimator", "status": "merged", "reviews": 2},
        {"id": 27, "title": "Civil load distribution fix", "status": "merged", "reviews": 1},
        {"id": 31, "title": "MATLAB hub UI", "status": "open", "reviews": 0},
    ]

    # ========== UPGRADED GITHUB EVIDENCE SECTION ==========
    def build_github_evidence():
        # Actual commit log entries tracking your precise repository history timeline
        commits = [
            {"hash": "6397261", "date": "2026-06-09", "msg": "Initial commit: Set up repository structure"},
            {"hash": "e84b2c1", "date": "2026-06-09", "msg": "feat: Integrated multi-tab navigation layout skeleton"},
            {"hash": "a4d9f10", "date": "2026-06-09", "msg": "feat: Added MathWorks certificate verification hub grid"},
            {"hash": "c2b8e54", "date": "2026-06-10", "msg": "docs: Refactored technical blog with AC parallel RLC resonance equations"}
        ]
        
        prs = [
            {"id": 1, "title": "Implement multi-tab responsive navigation layout", "status": "merged", "reviews": 2},
            {"id": 2, "title": "Add interactive certificate asset modals", "status": "merged", "reviews": 1},
            {"id": 3, "title": "Electronics concept technical documentation rewrite", "status": "open", "reviews": 0}
        ]

        # Full-screen interactive dialog view window for your Git screenshot asset
        git_dialog = ft.AlertDialog(
            content=ft.Image(src="/github_commits.png", fit=ft.BoxFit.CONTAIN, height=650),
            actions=[ft.TextButton("Close", on_click=lambda e: page.pop_dialog())]
        )

        # Dynamic table elements generation
        commit_table = ft.DataTable(
            columns=[ft.DataColumn(ft.Text("Hash")), ft.DataColumn(ft.Text("Date")), ft.DataColumn(ft.Text("Message"))],
            rows=[ft.DataRow(cells=[
                ft.DataCell(ft.Text(c["hash"], font_family="monospace", color=ft.Colors.BLUE_GREY_700)), 
                ft.DataCell(ft.Text(c["date"])), 
                ft.DataCell(ft.Text(c["msg"]))
            ]) for c in commits]
        )
        
        pr_rows = []
        for p in prs:
            badge = ft.Chip(
                label=ft.Text(p["status"], size=11, color=ft.Colors.GREEN_700 if p["status"]=="merged" else ft.Colors.ORANGE_700, weight=ft.FontWeight.BOLD), 
                bgcolor=ft.Colors.GREEN_100 if p["status"]=="merged" else ft.Colors.ORANGE_100
            )
            pr_rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(f"#{p['id']}")), ft.DataCell(ft.Text(p['title'])), ft.DataCell(badge), ft.DataCell(ft.Text(f"{p['reviews']} reviews"))]))
            
        pr_table = ft.DataTable(
            columns=[ft.DataColumn(ft.Text("ID")), ft.DataColumn(ft.Text("Title")), ft.DataColumn(ft.Text("Status")), ft.DataColumn(ft.Text("Reviews"))],
            rows=pr_rows
        )
        
        # Electronics Context Contribution Narrative Box
        # Updated Backend Database Narrative Box
        impact = ft.Container(
            content=ft.Column([
                ft.Text("💡 Impact Summary & Firebase Management", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                ft.Text("• Database Architecture: Structured NoSQL collections within Firebase Firestore to handle live data pipelines for the team's engineering calculator modules."),
                ft.Text("• Authentication & Security: Implemented secure user authentication rules to manage access control parameters across the 20-member team workspace repository."),
                ft.Text("• Electronics Integration: Programmed data serialization loops in Python to synchronize calculated AC parallel RLC network parameters directly with cloud instances."),
            ]), padding=15, border=ft.Border.all(1, ft.Colors.BLUE_100), bgcolor=ft.Colors.BLUE_50, border_radius=12, margin=ft.Margin.only(top=15)
        )

        return ft.Column([
            ft.Text("🔍 GitHub Evidence & Source Logs", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_900),
            ft.Text("Verifiable individual trace logs mapping repository operations directly to project modules.", size=14, color=ft.Colors.BLUE_GREY_500),
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
            
            # Interactive Visual Screenshot Card Component
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Icon(ft.icons.Icons.CAMERA_ALT, color=ft.Colors.BLUE_600),
                            ft.Text("Terminal Commit Log Verification Screenshot (Click to Enlarge)", weight=ft.FontWeight.BOLD)
                        ]),
                        ft.Container(
                            content=ft.Image(
                                src="/github_commits.png",
                                fit=ft.BoxFit.COVER,
                                error_content=ft.Icon(ft.icons.Icons.BROKEN_IMAGE, size=40, color=ft.Colors.GREY_400)
                            ),
                            height=180,
                            border_radius=6,
                            alignment=ft.Alignment.CENTER,
                            bgcolor=ft.Colors.GREY_50
                        )
                    ]),
                    padding=12,
                    on_click=lambda e: page.show_dialog(git_dialog),
                    ink=True
                )
            ),
            
            ft.Card(content=ft.Container(content=ft.Column([ft.Text("Commit History Ledger", weight=ft.FontWeight.BOLD, size=16), commit_table]), padding=12)),
            ft.Card(content=ft.Container(content=ft.Column([ft.Text("Pull Request Management Logs", weight=ft.FontWeight.BOLD, size=16), pr_table]), padding=12)),
            impact
        ], scroll=ft.ScrollMode.AUTO)

    tabs = ft.Tabs(
        length=4,
        expand=True,
        content=ft.Column(
            expand=True,
            controls=[
                ft.TabBar(
                    tabs=[
                        ft.Tab(label="📅 Timeline"),
                        ft.Tab(label="📊 MATLAB Hub"),
                        ft.Tab(label="✍️ Blog"),
                        ft.Tab(label="🐙 GitHub"),
                    ],
                ),
                ft.TabBarView(
                    expand=True,
                    controls=[
                        build_timeline(),
                        build_matlab_hub(),
                        build_blog(),
                        build_github_evidence(),
                    ],
                ),
            ],
        ),
    )

    # ========== PROFESSIONALLY BRANDED ENGINEERING HEADER ==========
    header = ft.Container(
        content=ft.Row([
            # Left Accent: Engineering Role Badge Info
            ft.Column([
                ft.Row([
                    ft.Icon(ft.icons.Icons.LOCAL_FIRE_DEPARTMENT_ROUNDED, color=ft.Colors.AMBER_600, size=32),
                    ft.Text("Quotation App  – Collaborative Engineering Platform", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                ], spacing=10),
                ft.Row([
                    ft.Container(
                        content=ft.Text("ROLE: FIREBASE MANAGER", size=11, color=ft.Colors.AMBER_900, weight=ft.FontWeight.BOLD),
                        bgcolor=ft.Colors.AMBER_100,
                        padding=ft.Padding(left=10, top=4, right=10, bottom=4),
                        border_radius=4,
                    ),
                    ft.Text("| BENHARD HANDURA KARUMBONA Portfolio", size=20, color=ft.Colors.BLUE_GREY_600, weight=ft.FontWeight.W_500),
                    ft.Text("| Discipline: Electronics & Computer Engineering", size=13, color=ft.Colors.BLUE_GREY_400, italic=True),
                ], spacing=10, alignment=ft.MainAxisAlignment.START),
            ], expand=True),
            
            # Right Accent: Grade Weighting Breakdown Panel
            ft.Container(
                content=ft.Column([
                ], horizontal_alignment=ft.CrossAxisAlignment.END),
                padding=8,
                border=ft.Border.all(1, ft.Colors.BLUE_GREY_100),
                border_radius=6,
                bgcolor=ft.Colors.GREY_50
            )
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER),
        padding=15, 
        bgcolor=ft.Colors.BLUE_50, 
        border_radius=12, 
        margin=ft.Margin.only(bottom=15),
        border=ft.Border.all(1, ft.Colors.BLUE_100)
    )

    # ========== PERSONAL PROFILE SIDEBAR COMPONENT ==========
    profile_panel = ft.Container(
        content=ft.Column([
            # Round Profile Picture Frame
            ft.Container(
                content=ft.Image(
                    src="/profile.png",
                            fit=ft.BoxFit.COVER,
                    error_content=ft.Icon(ft.icons.Icons.ACCOUNT_CIRCLE, size=120, color=ft.Colors.BLUE_GREY_200)
                ),
                width=140,
                height=140,
                border_radius=70, # Makes the container a perfect circle
                border=ft.Border.all(3, ft.Colors.BLUE_400), # Adds an engineering blue ring
                alignment=ft.Alignment.CENTER,
                shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.with_opacity(0.15, ft.Colors.BLACK))
            ),
            ft.Divider(height=5, color=ft.Colors.TRANSPARENT),
            
            # Name and Identifiers directly underneath the photo
            ft.Text("Benhard H. Karumbona", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
            ft.Text("Student ID: 225153238", size=12, font_family="monospace", color=ft.Colors.BLUE_GREY_600, text_align=ft.TextAlign.CENTER),
            
            ft.Divider(height=10, color=ft.Colors.GREY_300),
            
            # Technical Badges
            ft.Container(
                content=ft.Text("⚡ FIREBASE MANAGER", size=10, color=ft.Colors.AMBER_900, weight=ft.FontWeight.BOLD),
                bgcolor=ft.Colors.AMBER_100,
                padding=ft.Padding(left=12, top=5, right=12, bottom=5),
                border_radius=15,
            ),
            ft.Text("Electronics & Computer Engineering\nUniversity of Namibia", size=11, color=ft.Colors.BLUE_GREY_400, text_align=ft.TextAlign.CENTER, italic=True),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=6),
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        border=ft.Border.all(1, ft.Colors.GREY_200),
        width=240, # Fixed sidebar width
        alignment=ft.Alignment.TOP_CENTER
    )

    # ========== MAIN RESPONSIVE GRID HOLDER ==========
    # This arranges the Profile Panel on the left, and your Tabs layout on the right side side-by-side
    main_layout = ft.Row(
        controls=[
            profile_panel,     # Left Side: Your Photo & Name card
            ft.VerticalDivider(width=5, color=ft.Colors.TRANSPARENT),
            ft.Container(content=tabs, expand=True) # Right Side: The rest of your portfolio tabs
        ],
        vertical_alignment=ft.CrossAxisAlignment.START,
        expand=True
    )
    
    # Send the final structured view components directly to the web display canvas page
    page.add(header, main_layout)

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")


if __name__ == "__main__":
    # The view parameter tells Flet to run cleanly on web servers
    ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)
