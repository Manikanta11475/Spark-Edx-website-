import os

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

index_content = read_file('index.html')

# Find the boundaries
start_block = "    <!-- ======================= BLOCK 1: HERO SECTION ======================= -->"
end_block = "    <!-- ======================= BLOCK 6: CONVERSION FOOTER ======================= -->"

header_part = index_content.split(start_block)[0]
footer_part = end_block + index_content.split(end_block)[1]

# Make sure navbar active states and backgrounds are handled. 
# For non-index pages, we might want the navbar to have a solid background immediately, 
# or just add a padding top to the body. We can wrap content in a generic hero.

def generate_page(filename, title, content_html):
    # Replace title in header
    custom_header = header_part.replace("<title>Spark EdX — Premium English Literacy Programs for Schools in Andhra Pradesh</title>", f"<title>{title} | Spark EdX</title>")
    
    # Create a generic hero for inner pages
    inner_hero = f"""
    <!-- ======================= INNER PAGE HERO ======================= -->
    <section class="pt-32 pb-16 bg-navy-900 relative overflow-hidden">
        <div class="absolute inset-0 bg-brand-900/20"></div>
        <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="reveal font-display text-4xl sm:text-5xl font-bold text-white mb-4">{title}</h1>
            <div class="w-24 h-1 bg-brand-500 mx-auto rounded-full"></div>
        </div>
    </section>
    """
    
    page_content = custom_header + inner_hero + content_html + footer_part
    write_file(filename, page_content)

# 1. ABOUT US PAGE
about_content = """
    <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-2 gap-12 items-center mb-20">
                <div class="reveal">
                    <h2 class="font-display text-3xl md:text-4xl font-bold text-navy-900 mb-6">About Spark EdX</h2>
                    <p class="text-gray-600 text-lg leading-relaxed mb-6">Spark EdX is an innovative education platform dedicated to improving English literacy and communication in schools through technology-driven, research-based learning programs.</p>
                    <p class="text-gray-600 text-lg leading-relaxed">Our team of experienced educators and language specialists has designed structured, step-by-step learning solutions that make English learning engaging and effective for both teachers and students.</p>
                </div>
                <div class="reveal reveal-delay-1 relative rounded-2xl overflow-hidden shadow-2xl">
                    <img src="assets/images/brochure-2.jpg" alt="About Spark EdX" class="w-full h-auto object-cover" style="max-height: 400px; object-position: top;">
                </div>
            </div>

            <div class="reveal bg-gradient-to-r from-brand-600 to-navy-900 rounded-3xl p-10 text-center text-white mb-20">
                <h3 class="font-display text-2xl md:text-3xl font-bold mb-4">Empowering Students, Enriching Futures</h3>
                <p class="text-lg text-white/80 max-w-2xl mx-auto mb-8">Join the Spark EdX Partner Schools Network. Let's build confident readers, writers, and communicators — together!</p>
                <a href="contact.html" class="inline-block bg-white text-navy-900 px-8 py-3 rounded-full font-bold hover:bg-gray-100 transition-colors shadow-lg">Partner With Us</a>
            </div>

            <div class="text-center mb-16 reveal">
                <h2 class="font-display text-3xl font-bold text-navy-900">Our Leadership</h2>
                <div class="w-16 h-1 bg-brand-500 mx-auto rounded-full mt-4 mb-10"></div>
            </div>
            
            <div class="grid md:grid-cols-2 gap-10 max-w-4xl mx-auto">
                <!-- Director -->
                <div class="reveal card-hover bg-slate-50 rounded-2xl p-8 shadow-sm border border-slate-100 text-center">
                    <div class="w-32 h-32 mx-auto rounded-full overflow-hidden mb-6 border-4 border-white shadow-lg">
                        <img src="assets/images/director.png" alt="G V G Krishna" class="w-full h-full object-cover">
                    </div>
                    <h3 class="font-display font-bold text-xl text-navy-900 mb-1">G V G Krishna</h3>
                    <p class="text-brand-600 font-medium text-sm uppercase tracking-wider mb-4">Director</p>
                </div>

                <!-- Academic Head -->
                <div class="reveal reveal-delay-1 card-hover bg-slate-50 rounded-2xl p-8 shadow-sm border border-slate-100 text-center">
                    <div class="w-32 h-32 mx-auto rounded-full overflow-hidden mb-6 border-4 border-white shadow-lg">
                        <img src="assets/images/academic-head.png" alt="M. Abhiram gupta" class="w-full h-full object-cover">
                    </div>
                    <h3 class="font-display font-bold text-xl text-navy-900 mb-1">M. Abhiram gupta</h3>
                    <p class="text-brand-600 font-medium text-sm uppercase tracking-wider mb-4">Academic Head</p>
                </div>
            </div>
        </div>
    </section>
"""
generate_page('about.html', 'About Us', about_content)

# 2. PROGRAMS PAGE
programs_content = """
    <section class="py-20 bg-slate-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16 reveal">
                <h2 class="font-display text-3xl md:text-4xl font-bold text-navy-900 mb-4">Our Programs</h2>
                <p class="text-gray-600 text-lg max-w-2xl mx-auto">At Spark EdX, we empower young minds with essential life skills through interactive and engaging programs designed to boost confidence, communicative abilities, and academic success.</p>
            </div>

            <div class="grid md:grid-cols-2 gap-8 mb-20">
                <!-- Communicative English -->
                <div class="reveal bg-white rounded-2xl p-8 shadow-md border border-slate-100 flex gap-6">
                    <div class="w-16 h-16 rounded-xl bg-red-100 text-red-500 flex items-center justify-center shrink-0">
                        <i data-lucide="message-circle" class="w-8 h-8"></i>
                    </div>
                    <div>
                        <h3 class="font-display text-xl font-bold text-navy-900 mb-2">Communicative English</h3>
                        <p class="text-gray-600">Improve speaking, listening, and social skills through interactive fun activities.</p>
                    </div>
                </div>

                <!-- Phonics -->
                <div class="reveal reveal-delay-1 bg-white rounded-2xl p-8 shadow-md border border-slate-100 flex gap-6">
                    <div class="w-16 h-16 rounded-xl bg-green-100 text-green-500 flex items-center justify-center shrink-0">
                        <i data-lucide="book-open" class="w-8 h-8"></i>
                    </div>
                    <div>
                        <h3 class="font-display text-xl font-bold text-navy-900 mb-2">Phonics</h3>
                        <p class="text-gray-600">Master reading and writing with our phonics-based learning approach.</p>
                    </div>
                </div>
            </div>

            <div class="text-center mb-12 reveal">
                <h2 class="font-display text-3xl font-bold text-navy-900">Program Highlights</h2>
                <div class="w-16 h-1 bg-brand-500 mx-auto rounded-full mt-4 mb-10"></div>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-20">
                <div class="reveal bg-white p-6 rounded-xl shadow-sm border border-slate-100">
                    <div class="w-12 h-12 rounded-lg bg-red-50 text-red-500 flex items-center justify-center mb-4"><i data-lucide="users"></i></div>
                    <h4 class="font-bold text-navy-900 mb-2">Teacher Training Workshops</h4>
                    <p class="text-gray-600 text-sm">Equip your teachers with expert-level strategies to teach Phonics & Communication.</p>
                </div>
                <div class="reveal reveal-delay-1 bg-white p-6 rounded-xl shadow-sm border border-slate-100">
                    <div class="w-12 h-12 rounded-lg bg-green-50 text-green-500 flex items-center justify-center mb-4"><i data-lucide="video"></i></div>
                    <h4 class="font-bold text-navy-900 mb-2">7 Recorded Course Platform</h4>
                    <p class="text-gray-600 text-sm">Access engaging video lessons anytime.</p>
                </div>
                <div class="reveal reveal-delay-2 bg-white p-6 rounded-xl shadow-sm border border-slate-100">
                    <div class="w-12 h-12 rounded-lg bg-teal-50 text-teal-500 flex items-center justify-center mb-4"><i data-lucide="laptop"></i></div>
                    <h4 class="font-bold text-navy-900 mb-2">Dedicated School Website / LMS</h4>
                    <p class="text-gray-600 text-sm">Personalized portal for your school with student & teacher access.</p>
                </div>
                <div class="reveal bg-white p-6 rounded-xl shadow-sm border border-slate-100">
                    <div class="w-12 h-12 rounded-lg bg-amber-50 text-amber-500 flex items-center justify-center mb-4"><i data-lucide="file-text"></i></div>
                    <h4 class="font-bold text-navy-900 mb-2">Worksheets & Practice Materials</h4>
                    <p class="text-gray-600 text-sm">Printable resources for classroom and home practice.</p>
                </div>
                <div class="reveal reveal-delay-1 bg-white p-6 rounded-xl shadow-sm border border-slate-100">
                    <div class="w-12 h-12 rounded-lg bg-blue-50 text-blue-500 flex items-center justify-center mb-4"><i data-lucide="trending-up"></i></div>
                    <h4 class="font-bold text-navy-900 mb-2">Progress Tracking & Certificates</h4>
                    <p class="text-gray-600 text-sm">Monitor growth and celebrate achievement.</p>
                </div>
            </div>

            <div class="bg-navy-900 rounded-3xl p-10 md:p-16 text-white reveal shadow-xl">
                <div class="text-center mb-12">
                    <h2 class="font-display text-3xl font-bold mb-4">Why Choose Spark EdX?</h2>
                    <p class="text-white/70 max-w-2xl mx-auto">Transform the way your students learn to read, spell, write, and communicate!</p>
                </div>
                <div class="grid md:grid-cols-2 gap-8">
                    <div class="flex gap-4">
                        <div class="shrink-0 mt-1"><i data-lucide="check-circle" class="text-brand-400"></i></div>
                        <div>
                            <h4 class="font-bold text-lg mb-1">Experienced & Friendly Trainers</h4>
                            <p class="text-white/60 text-sm">Our passionate educators are dedicated to fostering a love for learning in children.</p>
                        </div>
                    </div>
                    <div class="flex gap-4">
                        <div class="shrink-0 mt-1"><i data-lucide="check-circle" class="text-brand-400"></i></div>
                        <div>
                            <h4 class="font-bold text-lg mb-1">Interactive & Fun Learning</h4>
                            <p class="text-white/60 text-sm">We make learning enjoyable with hands-on activities and engaging lessons.</p>
                        </div>
                    </div>
                    <div class="flex gap-4">
                        <div class="shrink-0 mt-1"><i data-lucide="check-circle" class="text-brand-400"></i></div>
                        <div>
                            <h4 class="font-bold text-lg mb-1">Activities Language for Life</h4>
                            <p class="text-white/60 text-sm">Participate in creative, engaging activities to develop cognitive & social skills.</p>
                        </div>
                    </div>
                    <div class="flex gap-4">
                        <div class="shrink-0 mt-1"><i data-lucide="check-circle" class="text-brand-400"></i></div>
                        <div>
                            <h4 class="font-bold text-lg mb-1">Stage Confidence</h4>
                            <p class="text-white/60 text-sm">Build public speaking skills and boost confidence to perform on stage.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
generate_page('programs.html', 'Programs', programs_content)

# 3. CONTACT PAGE
contact_content = """
    <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-2 gap-12">
                <div class="reveal">
                    <h2 class="font-display text-3xl font-bold text-navy-900 mb-6">Get in Touch</h2>
                    <p class="text-gray-600 mb-10">Interested in bringing Spark EdX to your school? Reach out to us today and let's build confident readers and communicators together.</p>
                    
                    <div class="space-y-6">
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 rounded-xl bg-brand-50 text-brand-600 flex items-center justify-center shrink-0">
                                <i data-lucide="map-pin"></i>
                            </div>
                            <div>
                                <h4 class="font-bold text-navy-900 mb-1">Location</h4>
                                <p class="text-gray-600">Spark EdX, Narasaraopet<br>Andhra Pradesh, India</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 rounded-xl bg-brand-50 text-brand-600 flex items-center justify-center shrink-0">
                                <i data-lucide="phone"></i>
                            </div>
                            <div>
                                <h4 class="font-bold text-navy-900 mb-1">Phone</h4>
                                <p class="text-gray-600">+91 9052581710<br>+91 9948203634</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 rounded-xl bg-brand-50 text-brand-600 flex items-center justify-center shrink-0">
                                <i data-lucide="mail"></i>
                            </div>
                            <div>
                                <h4 class="font-bold text-navy-900 mb-1">Email</h4>
                                <p class="text-gray-600">info@sparkedx.com</p>
                                <p class="text-gray-600">www.sparkedx.com</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="reveal reveal-delay-1 bg-slate-50 p-8 rounded-3xl border border-slate-100 shadow-lg">
                    <h3 class="font-display text-2xl font-bold text-navy-900 mb-6">Send an Inquiry</h3>
                    <form class="space-y-4">
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Name</label>
                            <input type="text" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-brand-500" placeholder="Your Name">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">School Name</label>
                            <input type="text" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-brand-500" placeholder="Your School">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Phone Number</label>
                            <input type="tel" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-brand-500" placeholder="Your Phone">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Message</label>
                            <textarea rows="4" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-brand-500" placeholder="How can we help?"></textarea>
                        </div>
                        <button type="button" class="w-full bg-brand-600 hover:bg-brand-700 text-white font-bold py-3 px-4 rounded-xl transition-colors">Send Message</button>
                    </form>
                </div>
            </div>
        </div>
    </section>
"""
generate_page('contact.html', 'Contact Us', contact_content)

# 4. BLOGS PAGE
blogs_content = """
    <section class="py-20 bg-slate-50 min-h-[60vh]">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16 reveal">
                <h2 class="font-display text-3xl md:text-4xl font-bold text-navy-900 mb-4">Latest Insights & Articles</h2>
                <p class="text-gray-600 text-lg max-w-2xl mx-auto">Discover modern teaching strategies, the importance of phonics, and ways to improve English literacy in your school.</p>
            </div>
            
            <div class="grid md:grid-cols-3 gap-8">
                <!-- Blog 1 -->
                <article class="reveal bg-white rounded-2xl overflow-hidden shadow-md border border-slate-100 card-hover">
                    <div class="h-48 bg-blue-100 flex items-center justify-center text-blue-400">
                        <i data-lucide="image" class="w-12 h-12"></i>
                    </div>
                    <div class="p-6">
                        <div class="text-sm text-brand-600 font-semibold mb-2">Education</div>
                        <h3 class="font-display text-xl font-bold text-navy-900 mb-3">Why Phonics is Essential for Early Readers</h3>
                        <p class="text-gray-600 text-sm mb-4">Understanding the connection between letters and sounds is the foundation of reading fluency...</p>
                        <a href="#" class="text-brand-600 font-medium text-sm hover:underline flex items-center gap-1">Read More <i data-lucide="arrow-right" class="w-4 h-4"></i></a>
                    </div>
                </article>

                <!-- Blog 2 -->
                <article class="reveal reveal-delay-1 bg-white rounded-2xl overflow-hidden shadow-md border border-slate-100 card-hover">
                    <div class="h-48 bg-amber-100 flex items-center justify-center text-amber-400">
                        <i data-lucide="image" class="w-12 h-12"></i>
                    </div>
                    <div class="p-6">
                        <div class="text-sm text-brand-600 font-semibold mb-2">Communication</div>
                        <h3 class="font-display text-xl font-bold text-navy-900 mb-3">Building Stage Confidence in Students</h3>
                        <p class="text-gray-600 text-sm mb-4">Public speaking is a crucial life skill. Here are 5 activities to help students overcome stage fright...</p>
                        <a href="#" class="text-brand-600 font-medium text-sm hover:underline flex items-center gap-1">Read More <i data-lucide="arrow-right" class="w-4 h-4"></i></a>
                    </div>
                </article>

                <!-- Blog 3 -->
                <article class="reveal reveal-delay-2 bg-white rounded-2xl overflow-hidden shadow-md border border-slate-100 card-hover">
                    <div class="h-48 bg-emerald-100 flex items-center justify-center text-emerald-400">
                        <i data-lucide="image" class="w-12 h-12"></i>
                    </div>
                    <div class="p-6">
                        <div class="text-sm text-brand-600 font-semibold mb-2">Technology</div>
                        <h3 class="font-display text-xl font-bold text-navy-900 mb-3">The Role of LMS in Modern Classrooms</h3>
                        <p class="text-gray-600 text-sm mb-4">How integrating a dedicated School Website and LMS can transform the learning experience...</p>
                        <a href="#" class="text-brand-600 font-medium text-sm hover:underline flex items-center gap-1">Read More <i data-lucide="arrow-right" class="w-4 h-4"></i></a>
                    </div>
                </article>
            </div>
        </div>
    </section>
"""
generate_page('blogs.html', 'Blogs', blogs_content)

print("Pages generated successfully.")
