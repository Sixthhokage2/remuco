package remuco.ui.simple;

import javax.microedition.lcdui.Form;

import remuco.data.Song;

/**
 * Represnetation of a song as a form.
 * 
 * @author Christian Buennig
 * 
 */
public class SongForm extends Form {

	private static final String[] RATING_STRINGS = new String[] { "-", "*",
			"**", "***", "****", "*****", "***** *", "***** **", "***** ***",
			"***** ****", "***** *****"};

	private static final int RATING_STRINGS_MAX = RATING_STRINGS.length - 1;

	private static final String[] EXTRA_TAGS = new String[] { Song.TAG_GENRE,
			Song.TAG_YEAR };

	private static final int EXTRA_TAGS_LEN = EXTRA_TAGS.length;

	private Song song;

	public SongForm(String title) {
		super(title);
	}

	public Song getSong() {
		return song;
	}

	public void setSong(Song s) {

		this.song = s;

		// remove current currentSong descriptions
		int n = this.size();
		for (int i = 0; i < n; i++) {
			this.delete(0);
		}

		if (s == null) {
			return;
		}

		final String lb = "\n";
		StringBuffer sb = new StringBuffer();

		sb.append(s.getTag(Song.TAG_TITLE)).append(" (").append(
				s.getTag(Song.TAG_ARTIST)).append(")");

		// write standard currentSong descriptions

		sb.delete(0, sb.length());
		sb.append(s.getTag(Song.TAG_ARTIST)).append(": ");
		sb.append(s.getTag(Song.TAG_TITLE));
		sb.append(" (").append(s.getTag(Song.TAG_ALBUM)).append(")");
		sb.append(lb);
		sb.append("Rating: ").append(ratingtoString(s.getRating()));
		sb.append(lb);
		sb.append("Length: ").append(s.getLenFormatted());

		// write extra song descriptions
		n = EXTRA_TAGS_LEN;
		for (int i = 0; i < n; i++) {
			sb.append(lb);
			sb.append(translateTagName(EXTRA_TAGS[i])).append(": ");
			sb.append(s.getTag(EXTRA_TAGS[i]));
		}

		this.append(sb.toString());

	}

	private String ratingtoString(int rating) {
		if (rating >= 0 && rating <= RATING_STRINGS_MAX) {
			return RATING_STRINGS[rating];
		} else if (rating == Song.RATING_NONE) {
			return "unrated";
		} else {
			return Integer.toString(rating);
		}
	}

	private String translateTagName(String tagName) {
		return tagName;
	}

}
