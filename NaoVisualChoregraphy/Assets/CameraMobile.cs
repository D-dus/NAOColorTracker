using UnityEngine;
using System.Collections;

public class CameraMobile : MonoBehaviour {
	public float rotationSpeed;
	public float TranslationSpeed;
	private float mArrowKeyVertical;
	private float mArrowKeyHorizontal;
	// Use this for initialization
	void Start () {
	
	}
	void Update()
	{
		mArrowKeyVertical = Input.GetAxis ("Vertical");
		mArrowKeyHorizontal = Input.GetAxis ("Horizontal");
		transform.Translate ( 0f, 0f,mArrowKeyVertical* Time.deltaTime*TranslationSpeed);
		transform.Rotate (0f, mArrowKeyHorizontal * Time.deltaTime*rotationSpeed,0f);
	}

}
