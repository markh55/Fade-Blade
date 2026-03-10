import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";

function Home() {
  return (
    <>
      <Navbar />
      <main>
        {/* Hero */}
        <section className="hero">
          <div className="hero-content">
            <h1>Fade & Blade</h1>
            <p>Traditional Barbershop</p>
            <Link to="/book">
              <button>Book Now</button>
            </Link>
          </div>
        </section>

        {/* Info Bar */}
        <section className="info-bar">
          <div>
            <span>📍</span>
            <p>Address</p>
          </div>
          <div>
            <span>📞</span>
            <p>Phone</p>
          </div>
          <div>
            <span>🕐</span>
            <p>Hours</p>
          </div>
        </section>

        {/* Our Work */}
        <section className="our-work">
          <h2>Our Work</h2>
          <div className="work-grid">
            {/* Images will come from Cloudinary via API */}
          </div>
        </section>

        {/* Services */}
        <section className="services">
          <h2>Browse Our Services</h2>
          <div className="services-grid">
            {/* Services will come from API */}
          </div>
        </section>

        {/* Why Choose Us */}
        <section className="why-us">
          <h2>Why Choose Us</h2>
        </section>

        {/* Map */}
        <section className="map"></section>
      </main>
    </>
  );
}

export default Home;
