import { Link } from "react-router-dom";
import type { CSSProperties } from "react";
import Navbar from "../components/Navbar";
import "./Home.css";

function Home() {
  // Replace with uploaded image URLs from your admin/API.
  const clientImages: string[] = [];
  const featuredSlots = Array.from(
    { length: 4 },
    (_, index) => clientImages[index] ?? null,
  );
  const extraImages = clientImages.slice(4);

  const extraColumns = Math.max(
    1,
    Math.ceil(Math.sqrt(extraImages.length || 1)),
  );
  const extraRows = Math.max(
    1,
    Math.ceil((extraImages.length || 1) / extraColumns),
  );
  const extraGridStyle = {
    "--extra-cols": extraColumns,
    "--extra-rows": extraRows,
  } as CSSProperties;

  return (
    <>
      <Navbar />
      <main>
        {/* Hero */}
        <section className="hero">
          <img src="/Hero.jpg" alt="Fade & Blade" />
          <div className="hero-content">
            <Link to="/book">
              <button className="hero-btn hero-btn-primary">
                Book an Appointment
              </button>
            </Link>
            <Link to="/services">
              <button className="hero-btn hero-btn-secondary">
                Browse Services
              </button>
            </Link>
          </div>
        </section>

        {/* Info Bar */}
        <section className="info-bar">
          <div className="info-item">
            <span className="info-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" role="img" focusable="false">
                <path d="M12 2C8.13 2 5 5.13 5 9c0 4.92 6.08 12.26 6.34 12.57a.85.85 0 0 0 1.32 0C12.92 21.26 19 13.92 19 9c0-3.87-3.13-7-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z" />
              </svg>
            </span>
            <p className="info-title">Address</p>
            <p className="info-detail">3696 Lynden Road, Lefroy</p>
            <p className="info-detail">Ontario Canada</p>
          </div>

          <div className="info-item">
            <span className="info-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" role="img" focusable="false">
                <path d="M20.46 15.3 16.9 14.9a2 2 0 0 0-1.7.57l-2.58 2.58a15.2 15.2 0 0 1-6.67-6.67l2.58-2.58a2 2 0 0 0 .57-1.7L8.7 3.54A2 2 0 0 0 6.72 2H4.3A2.3 2.3 0 0 0 2 4.47 19.53 19.53 0 0 0 19.53 22 2.3 2.3 0 0 0 22 19.7v-2.42a2 2 0 0 0-1.54-1.98Z" />
              </svg>
            </span>
            <p className="info-title">Phone</p>
            <p className="info-detail">+62 (123)-456-7890</p>
            <p className="info-detail">+62 (123)-456-7890</p>
          </div>

          <div className="info-item">
            <span className="info-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" role="img" focusable="false">
                <path d="M12 2a10 10 0 1 0 10 10A10.01 10.01 0 0 0 12 2Zm1 10.41 3.29 3.3-1.42 1.41L11 13.24V6h2Z" />
              </svg>
            </span>
            <p className="info-title">Hours</p>
            <p className="info-detail">Mon - Sat: 9AM - 8PM</p>
            <p className="info-detail">Sun: 9AM - 6PM</p>
          </div>
        </section>

        {/* Our Clients */}
        <section className="our-work">
          <h2>Our Clients</h2>
          <div className="work-grid work-grid--featured">
            {featuredSlots.map((imageUrl, index) => (
              <div
                key={`featured-slot-${index + 1}`}
                className={`work-grid-item work-grid-item--featured-${index + 1}`}
              >
                {imageUrl ? (
                  <img src={imageUrl} alt={`Client work ${index + 1}`} />
                ) : (
                  <span className="work-grid-placeholder">Client Photo</span>
                )}
              </div>
            ))}
          </div>

          {extraImages.length > 0 && (
            <div className="work-grid work-grid--extra" style={extraGridStyle}>
              {extraImages.map((imageUrl, index) => (
                <div
                  key={`${imageUrl}-${index + 4}`}
                  className="work-grid-item work-grid-item--extra"
                >
                  <img src={imageUrl} alt={`Client work ${index + 5}`} />
                </div>
              ))}
            </div>
          )}
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
